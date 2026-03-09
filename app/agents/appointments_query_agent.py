from app.database.connection import SessionLocal
from app.database.models import Appointment


def get_user_appointments(user):

    db = SessionLocal()

    appointments = db.query(Appointment).filter(
        Appointment.user == user
    ).all()

    db.close()

    if not appointments:
        return "Você não possui consultas agendadas."

    response = "Você possui as seguintes consultas:\n"

    for ap in appointments:
        response += f"📅 {ap.date}\n"

    return response