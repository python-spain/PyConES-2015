# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from schedule.views import ShowSchedule

urlpatterns = i18n_patterns(
    url(r'^$', ShowSchedule.as_view(), name="show"),
)
