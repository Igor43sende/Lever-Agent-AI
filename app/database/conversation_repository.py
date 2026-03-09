from app.database.connection import SessionLocal
from app.database.models import Conversation


def save_message(user, role, message):

    db = SessionLocal()

    conversation = Conversation(
        user=user,
        role=role,
        message=message
    )

    db.add(conversation)
    db.commit()
    db.close()


def get_conversation_history(user):

    db = SessionLocal()

    messages = db.query(Conversation).filter(
        Conversation.user == user
    ).order_by(Conversation.created_at).all()

    db.close()

    return messages