from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout_then_login
from django.contrib import admin
admin.autodiscover()
from views import UserProfileDetailView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',  login, name="login"),
    url(r'^logout/$', logout_then_login, name="logout"),
    url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile"),
)
