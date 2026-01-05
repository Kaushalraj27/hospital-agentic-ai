CREATE TABLE doctors_availability (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    day_of_week TEXT,
    time_slot TEXT,
    is_booked BOOLEAN
);

CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    medical_issue TEXT
);
