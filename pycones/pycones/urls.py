# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()

urlpatterns = i18n_patterns(
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^code-of-conduct/$', TemplateView.as_view(template_name='pages/code_of_conduct.html'), name="code_of_conduct"),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^schedule/', include('schedule.urls', namespace="schedule")),
)

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]
