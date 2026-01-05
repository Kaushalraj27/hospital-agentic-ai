import streamlit as st

from auth.login import login
from agents.intent_agent import classify_intent
from agents.symptom_agent import suggest_department
from agents.db_agent import get_available_doctors
from agents.booking_agent import book_slot
from agents.response_agent import generate_response
from agents.query_parser_agent import extract_department_and_day
from agents.patient_agent import save_patient


st.set_page_config(page_title="Hospital AI Assistant", layout="centered")

st.title("🏥 Hospital Agentic AI Assistant")


# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "patient_saved" not in st.session_state:
    st.session_state.patient_saved = False


# ---------------- LOGIN ----------------
if not st.session_state.logged_in:
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid login credentials")


# ---------------- PATIENT PROFILE ----------------
elif not st.session_state.patient_saved:
    st.subheader("🧑 Patient Details")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    issue = st.text_area("Describe your medical issue")

    if st.button("Save Patient Profile"):
        if name and issue:
            save_patient(name, int(age), issue)
            st.session_state.patient_saved = True
            st.success("Patient profile saved successfully!")
        else:
            st.warning("Please fill all required fields.")


# ---------------- MAIN QUERY INTERFACE ----------------
else:
    st.subheader("💬 Ask the Assistant")

    query = st.text_input("Enter your query")

    if st.button("Submit Query") and query:
        intent = classify_intent(query)

        # -------- SYMPTOM --------
        if intent == "SYMPTOM":
            department = suggest_department(query)
            result = department

        # -------- AVAILABILITY --------
        elif intent == "AVAILABILITY":
            department, day = extract_department_and_day(query)

            if not department or not day:
                result = []
            else:
                result = get_available_doctors(department, day)

        # -------- BOOKING --------
        elif intent == "BOOK":
            # Fixed parsing for TASK-1 demo
            success = book_slot(
                name="Dr Rahul",
                day="Monday",
                time_slot="09:00-10:00"
            )
            result = success

        else:
            result = None

        response = generate_response(intent, result)
        st.info(response)
