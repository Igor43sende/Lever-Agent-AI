from app.services.session_manager import update_session
from app.database.repository import create_appointment
from app.agents.reminder_agent import schedule_reminders


# inicia o fluxo de agendamento
def start_scheduling(session):

    session["state"] = "waiting_date"

    return "Para qual dia você deseja marcar a consulta?"


# finaliza o agendamento
def schedule_appointment(user, date, time):

    appointment = create_appointment(user, f"{date} {time}")

    schedule_reminders(user, f"{date} {time}")

    update_session(user, "idle")

    return f"Consulta marcada para {date} às {time}"