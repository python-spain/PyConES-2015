# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, translator

from sponsorship.models import SponsorLevel


class SponsorLevelTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(SponsorLevel, SponsorLevelTranslationOptions)
