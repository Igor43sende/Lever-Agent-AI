from app.services.intent_classifier import classify_intent
from app.services.session_manager import get_session
from app.agents.orchestrator_agent import orchestrate


def process_message(data):

    user = data.get("user")
    message = data.get("message")

    if not user or not message:
        return "Mensagem inválida."

    session = get_session(user)

    intent = classify_intent(message)

    return orchestrate(intent, user, message, session)