from app.services.session_manager import update_session
from app.database.repository import create_appointment
from app.agents.reminder_agent import schedule_reminders
from app.utils.date_parser import parse_date_time

# inicia o fluxo de agendamento
def start_scheduling(session):

    session["state"] = "waiting_date"

    return "Para qual dia você deseja marcar a consulta?"


# finaliza o agendamento
def schedule_appointment(user, date, time):

    parsed_datetime = parse_date_time(date, time)

    if not parsed_datetime:
        return "Não consegui entender a data ou horário."

    appointment = create_appointment(user, parsed_datetime)

    schedule_reminders(user, parsed_datetime)

    update_session(user, "idle")

    return f"Consulta marcada para {parsed_datetime}"