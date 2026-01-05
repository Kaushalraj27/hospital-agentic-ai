def generate_response(intent, result):
    """
    Generates user-friendly responses based on intent and agent outputs.
    """

    # ---------------- SYMPTOM RESPONSE ----------------
    if intent == "SYMPTOM":
        return (
            f"Based on your symptoms, you should consult the "
            f"{result} department."
        )

    # ---------------- AVAILABILITY RESPONSE ----------------
    if intent == "AVAILABILITY":
        if not result:
            return (
                "No available doctors found for the given "
                "department and day."
            )

        response = "Available doctors:\n"
        for doctor_name, time_slot in result:
            response += f"- {doctor_name} at {time_slot}\n"

        return response.strip()

    # ---------------- BOOKING RESPONSE ----------------
    if intent == "BOOK":
        if result:
            return "✅ Appointment booked successfully!"
        else:
            return (
                "❌ The selected slot is already booked. "
                "Please try a different time or doctor."
            )

    # ---------------- FALLBACK ----------------
    return (
        "I'm sorry, I couldn't understand your request. "
        "Please try again."
    )
