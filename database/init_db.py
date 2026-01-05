import sqlite3

conn = sqlite3.connect("database/hospital.db")
cursor = conn.cursor()

cursor.executescript(open("schema.sql").read())

doctors = [
    # Cardiology
    ("Dr Rahul", "Cardiology", "Monday", "09:00-10:00", 0),
    ("Dr Anjali", "Cardiology", "Tuesday", "10:00-11:00", 0),
    ("Dr Vikram", "Cardiology", "Wednesday", "11:00-12:00", 0),
    ("Dr Suman", "Cardiology", "Thursday", "12:00-13:00", 0),

    # Neurology
    ("Dr Meena", "Neurology", "Monday", "09:00-10:00", 0),
    ("Dr Rakesh", "Neurology", "Tuesday", "10:00-11:00", 0),
    ("Dr Kavita", "Neurology", "Wednesday", "11:00-12:00", 0),
    ("Dr Arjun", "Neurology", "Friday", "12:00-13:00", 0),

    # Orthopedics
    ("Dr Amit", "Orthopedics", "Monday", "10:00-11:00", 0),
    ("Dr Neeraj", "Orthopedics", "Tuesday", "11:00-12:00", 0),
    ("Dr Pooja", "Orthopedics", "Thursday", "09:00-10:00", 0),
    ("Dr Kunal", "Orthopedics", "Friday", "10:00-11:00", 0),

    # Pediatrics
    ("Dr Neha", "Pediatrics", "Monday", "11:00-12:00", 0),
    ("Dr Shalini", "Pediatrics", "Wednesday", "09:00-10:00", 0),
    ("Dr Aman", "Pediatrics", "Thursday", "10:00-11:00", 0),
    ("Dr Ritu", "Pediatrics", "Friday", "11:00-12:00", 0),

    # Dermatology
    ("Dr Sonia", "Dermatology", "Monday", "12:00-13:00", 0),
    ("Dr Alok", "Dermatology", "Tuesday", "09:00-10:00", 0),
    ("Dr Nisha", "Dermatology", "Wednesday", "10:00-11:00", 0),
    ("Dr Sameer", "Dermatology", "Thursday", "11:00-12:00", 0),

    # General Medicine
    ("Dr Ramesh", "General Medicine", "Monday", "09:00-10:00", 0),
    ("Dr Sunita", "General Medicine", "Tuesday", "10:00-11:00", 0),
    ("Dr Mohan", "General Medicine", "Wednesday", "11:00-12:00", 0),
    ("Dr Aarti", "General Medicine", "Thursday", "12:00-13:00", 0),
    ("Dr Prakash", "General Medicine", "Friday", "09:00-10:00", 0),
]


cursor.executemany("""
INSERT INTO doctors_availability
(name, department, day_of_week, time_slot, is_booked)
VALUES (?, ?, ?, ?, ?)
""", doctors)

conn.commit()
conn.close()

print("Database initialized successfully")
