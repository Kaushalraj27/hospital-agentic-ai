import sqlite3

DB_PATH = "database/hospital.db"

def book_slot(name, day, time_slot):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE doctors_availability
    SET is_booked=1
    WHERE name=? AND day_of_week=? AND time_slot=? AND is_booked=0
    """, (name, day, time_slot))

    conn.commit()
    success = cursor.rowcount
    conn.close()

    return success > 0
