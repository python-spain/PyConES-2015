# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from schedule.models import Schedule


def schedule_active(request):
    is_schedule_active = Schedule.objects.filter(published=True).exists()
    return {
        "is_schedule_active": is_schedule_active
    }
