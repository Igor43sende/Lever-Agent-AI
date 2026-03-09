import dateparser


def parse_date_time(date_text, time_text):

    combined = f"{date_text} {time_text}"

    parsed = dateparser.parse(
        combined,
        languages=["pt"]
    )

    if not parsed:
        return None

    return parsed