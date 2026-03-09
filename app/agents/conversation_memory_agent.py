from app.database.conversation_repository import save_message


def store_user_message(user, message):

    save_message(user, "user", message)


def store_assistant_message(user, message):

    save_message(user, "assistant", message)