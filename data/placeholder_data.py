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
    # MJPTBC colleges
    "MJPTBC Adilabad": [
        {"name": "Aarav Sharma", "stream": "B.Sc. Physics"},
        {"name": "Priya Gupta", "stream": "B.Sc. Chemistry"},
        {"name": "Rohan Mehta", "stream": "B.Sc. Mathematics"},
    ],
    "MJPTBC Ghanpur": [
        {"name": "Ananya Reddy", "stream": "B.Sc. Zoology"},
        {"name": "Kavya Singh", "stream": "B.Sc. Botany"},
        {"name": "Manish Kumar", "stream": "B.Sc. Computer Science"},
    ],
    "MJPTBC Hyderabad_Keesara": [
        {"name": "Diya Nair", "stream": "B.Sc. Physics"},
        {"name": "Fatima Khan", "stream": "B.Sc. Chemistry"},
        {"name": "Ishita Patel", "stream": "B.Sc. Mathematics"},
    ],
    "MJPTBC Jogulamba Gadwal": [
        {"name": "Meera Sharma", "stream": "B.Sc. Zoology"},
        {"name": "Nandini Rao", "stream": "B.Sc. Botany"},
        {"name": "Rhea Banerjee", "stream": "B.Sc. Biotechnology"},
    ],
    "MJPTBC Kamareddy": [
        {"name": "Arjun Malhotra", "stream": "B.Sc. Physics"},
        {"name": "Dev Chauhan", "stream": "B.Sc. Chemistry"},
        {"name": "Harsh Pandey", "stream": "B.Sc. Mathematics"},
    ],
    "MJPTBC Khammam": [
        {"name": "Kabir Dhawan", "stream": "B.Sc. Zoology"},
        {"name": "Lakshmi Iyer", "stream": "B.Sc. Botany"},
        {"name": "Sanya Arora", "stream": "B.Sc. Computer Science"},
    ],
    "MJPTBC Mahabubabad": [
        {"name": "Tanvi Bhatia", "stream": "B.Sc. Physics"},
        {"name": "Aditi Choudhary", "stream": "B.Sc. Chemistry"},
        {"name": "Bhavna Mishra", "stream": "B.Sc. Mathematics"},
    ],
    "MJPTBC Medhcal_Keesara": [
        {"name": "Charvi Aggarwal", "stream": "B.Sc. Zoology"},
        {"name": "Deepika Yadav", "stream": "B.Sc. Botany"},
        {"name": "Arnav Srivastava", "stream": "B.Sc. Biotechnology"},
    ],
    "MJPTBC Mulugu": [
        {"name": "Gaurav Thakur", "stream": "B.Sc. Physics"},
        {"name": "Kunal Jain", "stream": "B.Sc. Chemistry"},
        {"name": "Aisha Siddiqui", "stream": "B.Sc. Mathematics"},
    ],
    "MJPTBC Nizamabad": [
        {"name": "Divya Menon", "stream": "B.Sc. Zoology"},
        {"name": "Kriti Sharma", "stream": "B.Sc. Botany"},
        {"name": "Pooja Rathi", "stream": "B.Sc. Computer Science"},
    ],
    "MJPTBC Pedapalli": [
        {"name": "Saumya Kulkarni", "stream": "B.Sc. Physics"},
        {"name": "Aditya Kumar", "stream": "B.Sc. Chemistry"},
        {"name": "Priya Verma", "stream": "B.Sc. Mathematics"},
    ],
    "MJPTBC Sangareddy": [
        {"name": "Rohan Gupta", "stream": "B.Sc. Zoology"},
        {"name": "Sneha Patel", "stream": "B.Sc. Botany"},
        {"name": "Vikram Singh", "stream": "B.Sc. Biotechnology"},
    ],
    "MJPTBC Suryapet": [
        {"name": "Ananya Joshi", "stream": "B.Sc. Physics"},
        {"name": "Kavya Reddy", "stream": "B.Sc. Chemistry"},
        {"name": "Manish Tiwari", "stream": "B.Sc. Mathematics"},
    ],
    "MJPTBC Wargal": [
        {"name": "Diya Kapoor", "stream": "B.Sc. Zoology"},
        {"name": "Fatima Khan", "stream": "B.Sc. Botany"},
        {"name": "Ishita Nair", "stream": "B.Sc. Computer Science"},
    ],
    # TSWRD
    "TSWRD Pharmacy College, Mahbubabad": [
        {"name": "Meera Patel", "stream": "B.Pharm"},
        {"name": "Nandini Rao", "stream": "B.Pharm"},
        {"name": "Rhea Banerjee", "stream": "B.Pharm"},
    ],
    # TSWRDC
    "TSWRDC & PGC, Budvel": [
        {"name": "Arjun Malhotra", "stream": "B.Sc. Physics"},
        {"name": "Dev Chauhan", "stream": "B.Sc. Chemistry"},
        {"name": "Harsh Pandey", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDC Khammam": [
        {"name": "Kabir Dhawan", "stream": "B.Sc. Zoology"},
        {"name": "Lakshmi Iyer", "stream": "B.Sc. Botany"},
        {"name": "Sanya Arora", "stream": "B.Sc. Computer Science"},
    ],
    "TSWRDC Mahendrahills": [
        {"name": "Tanvi Bhatia", "stream": "B.Sc. Physics"},
        {"name": "Aditi Choudhary", "stream": "B.Sc. Chemistry"},
        {"name": "Bhavna Mishra", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDC Nirmal": [
        {"name": "Charvi Aggarwal", "stream": "B.Sc. Zoology"},
        {"name": "Deepika Yadav", "stream": "B.Sc. Botany"},
        {"name": "Arnav Srivastava", "stream": "B.Sc. Biotechnology"},
    ],
    "TSWRDC Nizamabad": [
        {"name": "Gaurav Thakur", "stream": "B.Sc. Physics"},
        {"name": "Kunal Jain", "stream": "B.Sc. Chemistry"},
        {"name": "Aisha Siddiqui", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDC Siddipet": [
        {"name": "Divya Menon", "stream": "B.Sc. Zoology"},
        {"name": "Kriti Sharma", "stream": "B.Sc. Botany"},
        {"name": "Pooja Rathi", "stream": "B.Sc. Computer Science"},
    ],
    # TSWRDCW
    "TSWRDCW Adilabad": [
        {"name": "Saumya Kulkarni", "stream": "B.Sc. Physics"},
        {"name": "Aditya Kumar", "stream": "B.Sc. Chemistry"},
        {"name": "Priya Verma", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Armoor": [
        {"name": "Rohan Gupta", "stream": "B.Sc. Zoology"},
        {"name": "Sneha Patel", "stream": "B.Sc. Botany"},
        {"name": "Vikram Singh", "stream": "B.Sc. Biotechnology"},
    ],
    "TSWRDCW Bhongir": [
        {"name": "Ananya Joshi", "stream": "B.Sc. Physics"},
        {"name": "Kavya Reddy", "stream": "B.Sc. Chemistry"},
        {"name": "Manish Tiwari", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Bhupalpally": [
        {"name": "Diya Kapoor", "stream": "B.Sc. Zoology"},
        {"name": "Fatima Khan", "stream": "B.Sc. Botany"},
        {"name": "Ishita Nair", "stream": "B.Sc. Computer Science"},
    ],
    "TSWRDCW Jagathgirigutta": [
        {"name": "Meera Patel", "stream": "B.Sc. Physics"},
        {"name": "Nandini Rao", "stream": "B.Sc. Chemistry"},
        {"name": "Rhea Banerjee", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Jagtial": [
        {"name": "Arjun Malhotra", "stream": "B.Sc. Zoology"},
        {"name": "Dev Chauhan", "stream": "B.Sc. Botany"},
        {"name": "Harsh Pandey", "stream": "B.Sc. Biotechnology"},
    ],
    "TSWRDCW Kamareddy": [
        {"name": "Kabir Dhawan", "stream": "B.Sc. Physics"},
        {"name": "Lakshmi Iyer", "stream": "B.Sc. Chemistry"},
        {"name": "Sanya Arora", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Karimnagar": [
        {"name": "Tanvi Bhatia", "stream": "B.Sc. Zoology"},
        {"name": "Aditi Choudhary", "stream": "B.Sc. Botany"},
        {"name": "Bhavna Mishra", "stream": "B.Sc. Computer Science"},
    ],
    "TSWRDCW Kothagudem": [
        {"name": "Charvi Aggarwal", "stream": "B.Sc. Physics"},
        {"name": "Deepika Yadav", "stream": "B.Sc. Chemistry"},
        {"name": "Arnav Srivastava", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Mahbubnagar": [
        {"name": "Gaurav Thakur", "stream": "B.Sc. Zoology"},
        {"name": "Kunal Jain", "stream": "B.Sc. Botany"},
        {"name": "Aisha Siddiqui", "stream": "B.Sc. Biotechnology"},
    ],
    "TSWRDCW Mancherial": [
        {"name": "Divya Menon", "stream": "B.Sc. Physics"},
        {"name": "Kriti Sharma", "stream": "B.Sc. Chemistry"},
        {"name": "Pooja Rathi", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Medak": [
        {"name": "Saumya Kulkarni", "stream": "B.Sc. Zoology"},
        {"name": "Aditya Kumar", "stream": "B.Sc. Botany"},
        {"name": "Priya Verma", "stream": "B.Sc. Computer Science"},
    ],
    "TSWRDCW Nagarkurnool": [
        {"name": "Rohan Gupta", "stream": "B.Sc. Physics"},
        {"name": "Sneha Patel", "stream": "B.Sc. Chemistry"},
        {"name": "Vikram Singh", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Nalgonda": [
        {"name": "Ananya Joshi", "stream": "B.Sc. Zoology"},
        {"name": "Kavya Reddy", "stream": "B.Sc. Botany"},
        {"name": "Manish Tiwari", "stream": "B.Sc. Biotechnology"},
    ],
    "TSWRDCW Sircilla": [
        {"name": "Diya Kapoor", "stream": "B.Sc. Physics"},
        {"name": "Fatima Khan", "stream": "B.Sc. Chemistry"},
        {"name": "Ishita Nair", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Suryapet": [
        {"name": "Meera Patel", "stream": "B.Sc. Zoology"},
        {"name": "Nandini Rao", "stream": "B.Sc. Botany"},
        {"name": "Rhea Banerjee", "stream": "B.Sc. Computer Science"},
    ],
    "TSWRDCW Vikarabad": [
        {"name": "Arjun Malhotra", "stream": "B.Sc. Physics"},
        {"name": "Dev Chauhan", "stream": "B.Sc. Chemistry"},
        {"name": "Harsh Pandey", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Wanaparthy": [
        {"name": "Kabir Dhawan", "stream": "B.Sc. Zoology"},
        {"name": "Lakshmi Iyer", "stream": "B.Sc. Botany"},
        {"name": "Sanya Arora", "stream": "B.Sc. Biotechnology"},
    ],
    "TSWRDCW Warangal east": [
        {"name": "Tanvi Bhatia", "stream": "B.Sc. Physics"},
        {"name": "Aditi Choudhary", "stream": "B.Sc. Chemistry"},
        {"name": "Bhavna Mishra", "stream": "B.Sc. Mathematics"},
    ],
    "TSWRDCW Warangal West": [
        {"name": "Charvi Aggarwal", "stream": "B.Sc. Zoology"},
        {"name": "Deepika Yadav", "stream": "B.Sc. Botany"},
        {"name": "Arnav Srivastava", "stream": "B.Sc. Computer Science"},
    ],
    # TTWRDC
    "TTWRDC Asifabad": [
        {"name": "Gaurav Thakur", "stream": "B.Sc. Physics"},
        {"name": "Kunal Jain", "stream": "B.Sc. Chemistry"},
        {"name": "Aisha Siddiqui", "stream": "B.Sc. Mathematics"},
    ],
    "TTWRDC Dammapeta": [
        {"name": "Divya Menon", "stream": "B.Sc. Zoology"},
        {"name": "Kriti Sharma", "stream": "B.Sc. Botany"},
        {"name": "Pooja Rathi", "stream": "B.Sc. Biotechnology"},
    ],
    "TTWRDC Devarakonda": [
        {"name": "Saumya Kulkarni", "stream": "B.Sc. Physics"},
        {"name": "Aditya Kumar", "stream": "B.Sc. Chemistry"},
        {"name": "Priya Verma", "stream": "B.Sc. Mathematics"},
    ],
    "TTWRDC Janagaon": [
        {"name": "Rohan Gupta", "stream": "B.Sc. Zoology"},
        {"name": "Sneha Patel", "stream": "B.Sc. Botany"},
        {"name": "Vikram Singh", "stream": "B.Sc. Computer Science"},
    ],
    "TTWRDC Khammam": [
        {"name": "Ananya Joshi", "stream": "B.Sc. Physics"},
        {"name": "Kavya Reddy", "stream": "B.Sc. Chemistry"},
        {"name": "Manish Tiwari", "stream": "B.Sc. Mathematics"},
    ],
    "TTWRDC Kothagudem": [
        {"name": "Diya Kapoor", "stream": "B.Sc. Zoology"},
        {"name": "Fatima Khan", "stream": "B.Sc. Botany"},
        {"name": "Ishita Nair", "stream": "B.Sc. Biotechnology"},
    ],
    "TTWRDC Mahabubabad": [
        {"name": "Meera Patel", "stream": "B.Sc. Physics"},
        {"name": "Nandini Rao", "stream": "B.Sc. Chemistry"},
        {"name": "Rhea Banerjee", "stream": "B.Sc. Mathematics"},
    ],
    "TTWRDC Mahabubnagar": [
        {"name": "Arjun Malhotra", "stream": "B.Sc. Zoology"},
        {"name": "Dev Chauhan", "stream": "B.Sc. Botany"},
        {"name": "Harsh Pandey", "stream": "B.Sc. Computer Science"},
    ],
    "TTWRDC Medak": [
        {"name": "Kabir Dhawan", "stream": "B.Sc. Physics"},
        {"name": "Lakshmi Iyer", "stream": "B.Sc. Chemistry"},
        {"name": "Sanya Arora", "stream": "B.Sc. Mathematics"},
    ],
    "TTWRDC Mulugu": [
        {"name": "Tanvi Bhatia", "stream": "B.Sc. Zoology"},
        {"name": "Aditi Choudhary", "stream": "B.Sc. Botany"},
        {"name": "Bhavna Mishra", "stream": "B.Sc. Biotechnology"},
    ],
    "TTWRDC Nizamabad": [
        {"name": "Charvi Aggarwal", "stream": "B.Sc. Physics"},
        {"name": "Deepika Yadav", "stream": "B.Sc. Chemistry"},
        {"name": "Arnav Srivastava", "stream": "B.Sc. Mathematics"},
    ],
    "TTWRDC Shadnagar": [
        {"name": "Gaurav Thakur", "stream": "B.Sc. Zoology"},
        {"name": "Kunal Jain", "stream": "B.Sc. Botany"},
        {"name": "Aisha Siddiqui", "stream": "B.Sc. Computer Science"},
    ],
    "TTWRDC Sircilla": [
        {"name": "Divya Menon", "stream": "B.Sc. Physics"},
        {"name": "Kriti Sharma", "stream": "B.Sc. Chemistry"},
        {"name": "Pooja Rathi", "stream": "B.Sc. Mathematics"},
    ],
    "TTWRDC Suryapeta": [
        {"name": "Saumya Kulkarni", "stream": "B.Sc. Zoology"},
        {"name": "Aditya Kumar", "stream": "B.Sc. Botany"},
        {"name": "Priya Verma", "stream": "B.Sc. Biotechnology"},
    ],
    "TTWRDC Utnoor": [
        {"name": "Rohan Gupta", "stream": "B.Sc. Physics"},
        {"name": "Sneha Patel", "stream": "B.Sc. Chemistry"},
        {"name": "Vikram Singh", "stream": "B.Sc. Mathematics"},
    ],
}

# For colleges without sample data, return an empty list.
# The app gracefully handles this with a "No students found" message.
