#!/usr/bin/env python3
"""
Alternative script using the project's SQLAlchemy engine.
Run with: python -m scripts.fetch_students_and_create_attendance_sqlalchemy
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text, inspect
from sqlalchemy.exc import OperationalError

# Database credentials from .streamlit/secrets.toml
# Password VS@123 needs URL encoding for @ symbol
DB_URL = "postgresql://postgres:VS%40123@localhost:5433/She_for_STEM"

def main():
    print("Connecting to database via SQLAlchemy...")
    engine = create_engine(DB_URL, pool_pre_ping=True)
    
    try:
        with engine.connect() as conn:
            print("Connected successfully!")
            
            # Check all schemas and tables
            inspector = inspect(engine)
            schemas = inspector.get_schema_names()
            print(f"\nAvailable schemas: {schemas}")
            
            for schema in schemas:
                tables = inspector.get_table_names(schema=schema)
                incubator_tables = [t for t in tables if 'incubator' in t.lower()]
                if incubator_tables:
                    print(f"  Schema '{schema}' has incubator tables: {incubator_tables}")
            
            # Find incubator table - check public first as user mentioned
            target_schema = None
            target_table = None
            
            for schema in ['public', 'old']:
                if schema in schemas:
                    tables = inspector.get_table_names(schema=schema)
                    incubator_tables = [t for t in tables if 'incubator' in t.lower()]
                    if incubator_tables:
                        target_schema = schema
                        target_table = incubator_tables[0]
                        break
            
            if not target_schema:
                print("\nNo incubator table found in public or old schema")
                return
            
            print(f"\nUsing table: {target_schema}.{target_table}")
            
            # Fetch students
            query = text(f"""
                SELECT DISTINCT full_name, subject_area_abbreviation as stream
                FROM {target_schema}.{target_table}
                WHERE full_name IS NOT NULL
                ORDER BY full_name
            """)
            result = conn.execute(query)
            students = result.fetchall()
            
            print(f"\nFound {len(students)} students:")
            for student in students:
                print(f"  - {student.full_name} ({student.stream})")
            
            # Create attendance table in public schema
            create_sql = text("""
            CREATE TABLE IF NOT EXISTS public.attendance (
                id SERIAL PRIMARY KEY,
                student_id VARCHAR(50),
                student_name VARCHAR(255) NOT NULL,
                email VARCHAR(255),
                session_id VARCHAR(50),
                session_name VARCHAR(255),
                session_date DATE,
                duration_in_sec INTEGER DEFAULT 0,
                attendance VARCHAR(50) CHECK (attendance IN ('Present', 'Absent')),
                source_system VARCHAR(100) DEFAULT 'Vigyan Shaala App',
                college VARCHAR(255),
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );
            
            CREATE INDEX IF NOT EXISTS idx_attendance_session_date ON public.attendance(session_date);
            CREATE INDEX IF NOT EXISTS idx_attendance_student_name ON public.attendance(student_name);
            CREATE INDEX IF NOT EXISTS idx_attendance_college ON public.attendance(college);
            """)
            
            conn.execute(create_sql)
            conn.commit()
            print("\nAttendance table created in public schema with indexes")
            
    except OperationalError as e:
        print(f"Database connection failed: {e}")
        print("   Make sure PostgreSQL is running on localhost:5433")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()