from app.services.session_manager import update_session
from app.services.scheduler_service import get_available_slots
from app.agents.scheduling_agent import schedule_appointment
from app.agents.cancel_agent import cancel_appointment
from app.agents.appointments_query_agent import get_user_appointments


def orchestrate(intent, user, message, session):

    state = session.get("state")

    # fluxo de agendamento
    if state == "waiting_date":

        slots = get_available_slots(message)

        update_session(user, "waiting_time", {"date": message})

        return f"Temos os seguintes horários disponíveis:\n{', '.join(slots)}"

    if state == "waiting_time":

        date = session["context"]["date"]

        response = schedule_appointment(user, date, message)

        update_session(user, "idle")

        return response

    # iniciar agendamento
    if intent == "schedule":

        update_session(user, "waiting_date")

        return "Para qual dia você deseja marcar a consulta?"

    # cancelar consulta
    if intent == "cancel":

        return cancel_appointment(user)

    # consultar consultas
    if intent == "check_appointments":

        return get_user_appointments(user)

    # verificar horários disponíveis
    if intent == "check_availability":

        slots = get_available_slots(message)

        return f"Horários disponíveis:\n{', '.join(slots)}"

    # uso do contexto
    if intent == "unknown":

        message_lower = message.lower()

        if "mudar" in message_lower or "remarcar" in message_lower:
            return "Você deseja remarcar sua consulta?"

    return "Não entendi sua solicitação."