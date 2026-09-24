# Vigyan Shaala — NEW BATCH August 2026: Attendance

A Streamlit web application for collecting student attendance data, replicating the functionality of the corresponding Google Form with a modern, branded UI.

## Features

- **Multi-section form** — Step 1: Select date & college → Step 2: Mark attendance → Step 3: Success confirmation
- **Dynamic attendance grid** — Shows students for the selected college with Present/Absent radio buttons
- **Quick actions** — Mark All Present, Mark All Absent, Reset All buttons
- **Live stats** — Real-time counters for Present, Absent, Unmarked, Total
- **Form validation** — All students must be marked before submission
- **PostgreSQL storage** — Submits attendance records to a PostgreSQL database (placeholder mode until DB is connected)
- **Responsive UI** — Mobile-friendly dark-themed design with Vigyan Shaala branding

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure database credentials

Edit `.streamlit/secrets.toml` with your PostgreSQL credentials:

```toml
DB_HOST = "your-host"
DB_PORT = "5432"
DB_NAME = "your-db"
DB_USER = "your-user"
DB_PASSWORD = "your-password"
```

### 3. Run the app

```bash
python -m streamlit run app.py
```

## Project Structure

```
VS Streamlit/
├── app.py                        # Main entry point
├── db/
│   ├── connection.py             # SQLAlchemy engine
│   └── queries.py                # Data fetch functions
├── storage/
│   └── store_to_database.py      # Write attendance to DB
├── ui/
│   ├── header.py                 # Logo + title
│   └── style.py                  # Custom CSS
├── utils/
│   └── helper_functions.py       # Timestamps, validation
├── data/
│   └── placeholder_data.py       # Sample dropdown data
├── images.jpg                    # Vigyan Shaala logo
├── .streamlit/secrets.toml       # DB credentials
├── requirements.txt
└── README.md
```

## Connecting Real Data

1. Update `.streamlit/secrets.toml` with real PostgreSQL credentials
2. In `db/queries.py`, uncomment the real query lines and replace placeholder returns
3. In `storage/store_to_database.py`, uncomment the DB write block

All placeholder spots are marked with `# TODO` comments.
