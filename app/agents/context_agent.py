from app.database.conversation_repository import get_conversation_history


def get_recent_context(user, limit=5):

    history = get_conversation_history(user)

    if not history:
        return []

    recent_messages = history[-limit:]

    context = []

    for msg in recent_messages:
        context.append({
            "role": msg.role,
            "message": msg.message
        })

    return context