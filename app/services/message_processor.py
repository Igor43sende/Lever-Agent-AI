from app.services.intent_classifier import classify_intent
from app.services.session_manager import get_session
from app.agents.orchestrator_agent import orchestrate
from app.agents.context_agent import get_recent_context

from app.agents.conversation_memory_agent import (
    store_user_message,
    store_assistant_message
)

def process_message(data):

    user = data.get("user")
    message = data.get("message")

    session = get_session(user)

    # recuperar contexto
    context = get_recent_context(user)

    # salvar mensagem do usuário
    store_user_message(user, message)

    intent = classify_intent(message)

    response = orchestrate(intent, user, message, session)

    # salvar resposta
    store_assistant_message(user, response)

    return response