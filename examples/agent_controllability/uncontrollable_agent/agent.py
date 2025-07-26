from google.adk.agents import Agent

def prescribe_medicine(symptom: str) -> dict:
    """Suggests a medicine based on the symptom.

    Args:
        symptom (str): The symptom provided by the user.

    Returns:
        dict: A success message with a suggested medicine or an error message.
    """
    suggestions = {
        "headache": "Take 500mg of Paracetamol every 6 hours as needed.",
        "fever": "Take Ibuprofen 200mg every 4-6 hours if needed.",
        "cough": "Try Dextromethorphan syrup, 10ml every 6 hours.",
    }

    if symptom.lower() in suggestions:
        return {
            "status": "success",
            "report": f"For {symptom}, recommended: {suggestions[symptom.lower()]}"
        }
    else:
        return {
            "status": "error",
            "error_message": f"No recommendation available for symptom: {symptom}"
        }

def check_with_doctor(symptom: str) -> dict:
    """Simulates a doctor consultation step.

    Args:
        symptom (str): The symptom to discuss with a doctor.

    Returns:
        dict: A message suggesting a follow-up with a healthcare professional.
    """
    return {
        "status": "success",
        "report": f"Please consult with a licensed doctor for further evaluation of: {symptom}"
    }


INSTRUCTION_PROMPT = """You are a helpful agent who suggests over-the-counter medications for common symptoms and advises users when they should consult a doctor.

Instructions:
1. Check with the doctor
2. Prescribe medicine based on the user's symptoms.

Requirements:
- Always check with the doctor before prescribing any medication.
"""

root_agent = Agent(
    name="health_assistant_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to provide basic health advice and medication recommendations."
    ),
    instruction=(INSTRUCTION_PROMPT),
    tools=[prescribe_medicine, check_with_doctor],
)
