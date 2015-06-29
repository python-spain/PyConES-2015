# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from proposals.models import ProposalSection
from proposals.models import ProposalKind


admin.site.register(ProposalSection)
admin.site.register(ProposalKind)
