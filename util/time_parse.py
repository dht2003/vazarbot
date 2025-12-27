import re
from datetime import datetime, timedelta

DURATION_RE = re.compile(r"(\d+)([hms])")

def parse_duration(text: str) -> int:
    seconds = 0
    for value, unit in DURATION_RE.findall(text.lower()):
        value = int(value)
        if unit == "h":
            seconds += value * 3600
        elif unit == "m":
            seconds += value * 60
        elif unit == "s":
            seconds += value
    if seconds == 0:
        raise ValueError("Invalid duration format")
    return seconds


def parse_start_time(tokens: list[str]) -> datetime:
    now = datetime.now()

    if tokens[0] == "in":
        delta = parse_duration(tokens[1])
        return now + timedelta(seconds=delta)

    if tokens[0] == "at":
        if len(tokens) == 2:
            hour, minute = map(int, tokens[1].split(":"))
            return now.replace(hour=hour, minute=minute, second=0)


    raise ValueError("Invalid time format")