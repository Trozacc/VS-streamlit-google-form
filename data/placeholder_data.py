"""
Placeholder data for the Vigyan Shaala Attendance application.
TODO: Replace these constants with PostgreSQL queries once DB access is available.
"""

# ──────────────────────────────────────────────────────────────
# Live session dates — fetched from form
# ──────────────────────────────────────────────────────────────
SESSION_DATES = [
    "10 September, 2026",
    "17 September, 2026",
    "19 September, 2026",
    "21 September, 2026",
]

# ──────────────────────────────────────────────────────────────
# College names — all 56 colleges from the Google Form
# TODO: Replace with   SELECT DISTINCT college FROM <source_table>
# ──────────────────────────────────────────────────────────────
COLLEGES = [
    "MJPTBC Adilabad",
    "MJPTBC Ghanpur",
    "MJPTBC Hyderabad_Keesara",
    "MJPTBC Jogulamba Gadwal",
    "MJPTBC Kamareddy",
    "MJPTBC Khammam",
    "MJPTBC Mahabubabad",
    "MJPTBC Medhcal_Keesara",
    "MJPTBC Mulugu",
    "MJPTBC Nizamabad",
    "MJPTBC Pedapalli",
    "MJPTBC Sangareddy",
    "MJPTBC Suryapet",
    "MJPTBC Wargal",
    "TSWRD Pharmacy College, Mahbubabad",
    "TSWRDC & PGC, Budvel",
    "TSWRDC Khammam",
    "TSWRDC Mahendrahills",
    "TSWRDC Nirmal",
    "TSWRDC Nizamabad",
    "TSWRDC Siddipet",
    "TSWRDCW Adilabad",
    "TSWRDCW Armoor",
    "TSWRDCW Bhongir",
    "TSWRDCW Bhupalpally",
    "TSWRDCW Jagathgirigutta",
    "TSWRDCW Jagtial",
    "TSWRDCW Kamareddy",
    "TSWRDCW Karimnagar",
    "TSWRDCW Kothagudem",
    "TSWRDCW Mahbubnagar",
    "TSWRDCW Mancherial",
    "TSWRDCW Medak",
    "TSWRDCW Nagarkurnool",
    "TSWRDCW Nalgonda",
    "TSWRDCW Sircilla",
    "TSWRDCW Suryapet",
    "TSWRDCW Vikarabad",
    "TSWRDCW Wanaparthy",
    "TSWRDCW Warangal east",
    "TSWRDCW Warangal West",
    "TTWRDC Asifabad",
    "TTWRDC Dammapeta",
    "TTWRDC Devarakonda",
    "TTWRDC Janagaon",
    "TTWRDC Khammam",
    "TTWRDC Kothagudem",
    "TTWRDC Mahabubabad",
    "TTWRDC Mahabubnagar",
    "TTWRDC Medak",
    "TTWRDC Mulugu",
    "TTWRDC Nizamabad",
    "TTWRDC Shadnagar",
    "TTWRDC Sircilla",
    "TTWRDC Suryapeta",
    "TTWRDC Utnoor",
]

# ──────────────────────────────────────────────────────────────
# Students per college  — placeholder sample data
# TODO: Replace with   SELECT name, stream FROM <source_table>
#                       WHERE college = :college
#
# Format:  { "college_name": [ {"name": "Student Name", "stream": "Stream"}, ... ] }
# ──────────────────────────────────────────────────────────────
STUDENTS_BY_COLLEGE: dict[str, list[dict[str, str]]] = {
    # ── sample data for demonstration ──────────────────────────
    "Acharya Narendra Dev College": [
        {"name": "Aarav Sharma", "stream": "B.Sc. (Hons) Physics"},
        {"name": "Priya Gupta", "stream": "B.Sc. (Hons) Chemistry"},
        {"name": "Rohan Mehta", "stream": "B.Sc. (Hons) Mathematics"},
        {"name": "Sneha Verma", "stream": "B.Sc. (Hons) Zoology"},
        {"name": "Vikram Singh", "stream": "B.Sc. (Hons) Botany"},
    ],
    "Aditi Mahavidyalaya": [
        {"name": "Ananya Joshi", "stream": "B.A. (Hons) Hindi"},
        {"name": "Kavya Reddy", "stream": "B.Com. (Hons)"},
        {"name": "Manish Tiwari", "stream": "B.Sc. (Hons) Computer Science"},
    ],
    "Miranda House": [
        {"name": "Diya Kapoor", "stream": "B.A. (Hons) English"},
        {"name": "Fatima Khan", "stream": "B.Sc. (Hons) Physics"},
        {"name": "Ishita Nair", "stream": "B.A. (Hons) History"},
        {"name": "Meera Patel", "stream": "B.Sc. (Hons) Chemistry"},
        {"name": "Nandini Rao", "stream": "B.A. (Hons) Political Science"},
        {"name": "Rhea Banerjee", "stream": "B.Sc. (Hons) Mathematics"},
    ],
    "Hans Raj College": [
        {"name": "Aditya Kumar", "stream": "B.Sc. (Hons) Physics"},
        {"name": "Dev Chauhan", "stream": "B.Com. (Hons)"},
        {"name": "Harsh Pandey", "stream": "B.A. (Hons) Economics"},
        {"name": "Nikhil Saxena", "stream": "B.Sc. (Hons) Chemistry"},
    ],
    "Hindu College": [
        {"name": "Arjun Malhotra", "stream": "B.A. (Hons) English"},
        {"name": "Kabir Dhawan", "stream": "B.Sc. (Hons) Physics"},
        {"name": "Lakshmi Iyer", "stream": "B.Com. (Hons)"},
        {"name": "Sanya Arora", "stream": "B.A. (Hons) Philosophy"},
        {"name": "Tanvi Bhatia", "stream": "B.Sc. (Hons) Statistics"},
    ],
    "Gargi College": [
        {"name": "Aditi Choudhary", "stream": "B.A. (Hons) Psychology"},
        {"name": "Bhavna Mishra", "stream": "B.Sc. (Hons) Microbiology"},
        {"name": "Charvi Aggarwal", "stream": "B.Com. (Hons)"},
        {"name": "Deepika Yadav", "stream": "B.A. (Hons) Political Science"},
    ],
    "Ramjas College": [
        {"name": "Arnav Srivastava", "stream": "B.Sc. (Hons) Mathematics"},
        {"name": "Gaurav Thakur", "stream": "B.A. (Hons) History"},
        {"name": "Kunal Jain", "stream": "B.Com. (Hons)"},
    ],
    "Lady Shri Ram College for Women": [
        {"name": "Aisha Siddiqui", "stream": "B.A. (Hons) Economics"},
        {"name": "Divya Menon", "stream": "B.A. (Hons) Journalism"},
        {"name": "Kriti Sharma", "stream": "B.A. (Hons) Psychology"},
        {"name": "Pooja Rathi", "stream": "B.Com. (Hons)"},
        {"name": "Saumya Kulkarni", "stream": "B.A. (Hons) English"},
    ],
}

# For colleges without sample data, return an empty list.
# The app gracefully handles this with a "No students found" message.
