# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, translator

from proposals.models import ProposalKind, ProposalBase


class ProposalKindTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


class ProposalBaseTranslationOptions(TranslationOptions):
    fields = ('title', 'abstract', 'additional_notes')


translator.register(ProposalKind, ProposalKindTranslationOptions)
translator.register(ProposalBase, ProposalBaseTranslationOptions)
