from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in visits:
        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": timezone.localtime(visit.entered_at),
                "duration": format_duration(get_duration(visit)),
                "is_long": is_visit_long(visit),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, "storage_information.html", context)
