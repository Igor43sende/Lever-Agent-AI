from app.database.connection import SessionLocal
from app.database.models import Appointment


def cancel_appointment(user):

    db = SessionLocal()

    appointment = db.query(Appointment).filter(
        Appointment.user == user
    ).first()

    if not appointment:
        db.close()
        return "Você não possui consultas agendadas."

    db.delete(appointment)
    db.commit()

    db.close()

    return "Sua consulta foi cancelada."