from app.agents.scheduling_agent import start_scheduling
from app.agents.appointments_query_agent import get_user_appointments
from app.agents.cancel_agent import cancel_appointment
from app.agents.knowledge_agent import answer_question
from app.agents.availability_agent import get_available_slots


def route_intent(intent, user, message, session):

    if intent == "schedule":
        return start_scheduling(session)

    if intent == "check_availability":
        return get_available_slots(message)

    if intent == "cancel":
        return cancel_appointment(user)

    if intent == "check_appointments":
        return get_user_appointments(user)

    if intent == "question":
        return answer_question(message)

    return "Não entendi sua solicitação."