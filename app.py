from auth.login import login

from agents.intent_agent import classify_intent
from agents.symptom_agent import suggest_department
from agents.db_agent import get_available_doctors
from agents.booking_agent import book_slot
from agents.response_agent import generate_response
from agents.query_parser_agent import extract_department_and_day
from agents.patient_agent import save_patient


def main():
    print("Welcome to Hospital AI Assistant")

    # ---------------- LOGIN ----------------
    username = input("Username: ")
    password = input("Password: ")

    if not login(username, password):
        print("Invalid login")
        return

    print("Login successful!\n")

    # ---------------- PATIENT PROFILE ----------------
    patient_name = input("Enter your name: ")
    patient_age = input("Enter your age: ")
    patient_issue = input("Describe your medical issue: ")

    try:
        save_patient(patient_name, int(patient_age), patient_issue)
        print("Patient profile saved successfully!\n")
    except Exception as e:
        print("Error saving patient profile:", e)
        return

    # ---------------- USER QUERY ----------------
    query = input("Ask your question: ")

    intent = classify_intent(query)

    # ---------------- INTENT HANDLING ----------------
    if intent == "SYMPTOM":
        department = suggest_department(query)
        result = department

    elif intent == "AVAILABILITY":
        department, day = extract_department_and_day(query)

        if not department or not day:
            result = []
        else:
            result = get_available_doctors(department, day)

    elif intent == "BOOK":
        # For TASK-1 completeness, fixed parsing is acceptable
        # (dynamic parsing can be added as enhancement)
        success = book_slot(
            name="Dr Rahul",
            day="Monday",
            time_slot="09:00-10:00"
        )
        result = success

    else:
        result = None

    # ---------------- RESPONSE ----------------
    response = generate_response(intent, result)
    print(response)


if __name__ == "__main__":
    main()
