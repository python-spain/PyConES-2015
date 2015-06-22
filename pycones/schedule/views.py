# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View


class ShowSchedule(View):

    def get(self, request):
        return render(request, "schedule/show.html")
