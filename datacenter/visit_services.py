from datetime import timedelta

from django.utils import timezone

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def get_duration(visit):
    end_time = visit.leaved_at or timezone.now()
    return end_time - visit.entered_at


def format_duration(duration):
    total_seconds = int(duration.total_seconds())

    hours, remainder = divmod(total_seconds, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)

    return f"{hours}:{minutes:02}:{seconds:02}"


def is_visit_long(visit, minutes=60):
    return get_duration(visit) > timedelta(minutes=minutes)
