# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View

from proposals.forms import ProposalFrom


class SubmitProposalView(View):

    def get(self, request):
        form = ProposalFrom()
        return render(request, "proposals/create.html", {"form": form})

    def post(self, request):
        form = ProposalFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proposals:success")
        return render(request, "proposals/create.html", {"form": form})
