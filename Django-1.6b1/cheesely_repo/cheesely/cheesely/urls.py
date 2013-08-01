from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cheesely.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'),
    url(r'^$',
        TemplateView.as_view(template_name='home.html'),
        name='home'),
    url(r'^cheeses/', include('cheeses.urls', namespace="cheeses")),
    url(r'^accounts/', include('registration.backends.simple.urls',)),

    ) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT),
