#!/usr/bin/env python3
"""
Script to fetch student names from incubator 13 table and create attendance table in public schema.
Run this when PostgreSQL is accessible.
"""

import os
import sys
import psycopg2
from psycopg2.extras import RealDictCursor

# Database credentials from .streamlit/secrets.toml
DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "database": "She_for_STEM",
    "user": "postgres",
    "password": "VS@123"
}

def connect_db():
    """Establish database connection."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.OperationalError as e:
        print(f"❌ Database connection failed: {e}")
        print("   Make sure PostgreSQL is running on localhost:5433")
        return None

def find_incubator_table(conn):
    """Find the incubator 13 table in public or old schema."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        # Check public schema
        cur.execute("""
            SELECT table_name FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name ILIKE '%incubator%'
        """)
        public_tables = cur.fetchall()
        
        # Check old schema
        cur.execute("""
            SELECT table_name FROM information_schema.tables 
            WHERE table_schema = 'old' AND table_name ILIKE '%incubator%'
        """)
        old_tables = cur.fetchall()
    
    print(f"Tables in public schema matching 'incubator': {public_tables}")
    print(f"Tables in old schema matching 'incubator': {old_tables}")
    
    # Prefer public schema as user mentioned
    if public_tables:
        return "public", f'"{public_tables[0]["table_name"]}"'
    elif old_tables:
        return "old", f'"{old_tables[0]["table_name"]}"'
    return None, None

def fetch_students(conn, schema, table_name):
    """Fetch student names from the incubator table."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        query = f"""
            SELECT DISTINCT full_name, subject_area_abbreviation as stream
            FROM {schema}.{table_name}
            WHERE full_name IS NOT NULL
            ORDER BY full_name
        """
        cur.execute(query)
        students = cur.fetchall()
    
    print(f"\n[+] Found {len(students)} students in {schema}.{table_name}:")
    for student in students:
        print(f"  - {student['full_name']} ({student['stream']})")
    
    return students

def create_attendance_table(conn):
    """Create attendance table in public schema with new column structure."""
    create_sql = """
    CREATE TABLE IF NOT EXISTS public.student_attendence (
        "Timestamp" TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        "Date_of_live_secssion" DATE,
        "College_name" VARCHAR(255),
        "Name_of_student" VARCHAR(255) NOT NULL,
        "subject_area_abbrevation" VARCHAR(100),
        "attendence_status" VARCHAR(10)
    );
    
    CREATE INDEX IF NOT EXISTS idx_student_attendence_session_date ON public.student_attendence("Date_of_live_secssion");
    CREATE INDEX IF NOT EXISTS idx_student_attendence_student_name ON public.student_attendence("Name_of_student");
    CREATE INDEX IF NOT EXISTS idx_student_attendence_college ON public.student_attendence("College_name");
    """
    
    with conn.cursor() as cur:
        cur.execute(create_sql)
    conn.commit()
    print("\n[+] Attendance table created in public schema with new columns")

def main():
    print("[*] Connecting to database...")
    conn = connect_db()
    if not conn:
        sys.exit(1)
    
    try:
        print("[+] Connected successfully!")
        
        # Find incubator table
        schema, table_name = find_incubator_table(conn)
        if not schema:
            print("\n[-] No incubator table found in public or old schema")
            sys.exit(1)
        
        print(f"\n[*] Using table: {schema}.{table_name}")
        
        # Fetch students
        students = fetch_students(conn, schema, table_name)
        
        # Create attendance table in public schema
        create_attendance_table(conn)
        
        print("\n[+] Done!")
        
    except Exception as e:
        print(f"\n[-] Error: {e}")
        conn.rollback()
        sys.exit(1)
    finally:
        conn.close()

if __name__ == "__main__":
    main()