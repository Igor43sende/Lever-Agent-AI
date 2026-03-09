sessions = {}


def get_session(user_id: str):

    if user_id not in sessions:
        sessions[user_id] = {
            "state": "idle",
            "context": {}
        }

    return sessions[user_id]


def update_session(user_id, state, context=None):

    session = get_session(user_id)

    session["state"] = state

    if context:
        session["context"].update(context)

    sessions[user_id] = session

    return session