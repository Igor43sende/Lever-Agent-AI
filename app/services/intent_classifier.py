def classify_intent(message):

    message = message.lower()

    if "cancelar" in message or "cancel" in message:
        return "cancel"

    if "consulta" in message and ("tenho" in message or "quais" in message):
        return "check_appointments"

    if "horário" in message or "horarios" in message:
        return "check_availability"

    if "marcar" in message or "agendar" in message:
        return "schedule"

    return "unknown"