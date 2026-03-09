from app.database.connection import SessionLocal
from app.database.models import Appointment

AVAILABLE_SLOTS = [
    "09:00",
    "10:00",
    "11:00",
    "14:00",
    "15:00",
    "16:00"
]


def get_available_slots(date):

    db = SessionLocal()

    appointments = db.query(Appointment).filter(
        Appointment.date.like(f"{date}%")
    ).all()

    booked_times = []

    for appointment in appointments:
        parts = appointment.date.split(" ")

        if len(parts) > 1:
            time = parts[1]
            booked_times.append(time)

    db.close()

    available = []

    for slot in AVAILABLE_SLOTS:
        if slot not in booked_times:
            available.append(slot)

    return available