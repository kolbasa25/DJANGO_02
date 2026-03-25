from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from datacenter.models import Passcard, Visit
from datacenter.visit_services import (
    get_duration,
    format_duration,
    is_visit_long,
)


def passcard_info_view(request, passcode):
    this_passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=this_passcard)

    formatted_visits = []
    for visit in this_passcard_visits:
        formatted_visits.append(
            {
                "entered_at": timezone.localtime(visit.entered_at),
                "duration": format_duration(get_duration(visit)),
                "is_strange": is_visit_long(visit),
            }
        )

    context = {
        "this_passcard": this_passcard,
        "this_passcard_visits": formatted_visits,
    }
    return render(request, "passcard_info.html", context)
