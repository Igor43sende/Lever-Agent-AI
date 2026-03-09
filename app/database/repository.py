from app.database.connection import SessionLocal
from app.database.models import Appointment


def create_appointment(user, date):

    db = SessionLocal()

    appointment = Appointment(
        user=user,
        date=date
    )

    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    db.close()

    return appointment