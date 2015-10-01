# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View
from schedule.models import Schedule


class ShowSchedule(View):
    """Shows the schedule of the event."""

    def get(self, request):
        schedule = Schedule.objects.filter(published=True, hidden=False).first()
        data = {"days": []}
        for day in schedule.day_set.all():
            data["days"].append({
                "date": day.date,
                "slots": day.slot_set.all().select_related()
            })
        return render(request, "schedule/show.html", data)
