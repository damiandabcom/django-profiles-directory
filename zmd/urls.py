from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from django.contrib.auth.views import (
   password_reset, 
   password_reset_done,
   password_reset_confirm,
   password_reset_complete
)


from profiles.backends import MyRegistrationView
from profiles import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^profiles/$', RedirectView.as_view(pattern_name='browse', permanent=True)),
    url(r'^profiles/(?P<slug>[-\w]+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profiles/(?P<slug>[-\w]+)/edit/$', views.edit_profile, name='edit_profile'),

    url(r'^browse/$', RedirectView.as_view(pattern_name='browse', permanent=True)),
	url(r'^browse/name/$',
	    views.browse_by_name, name='browse'),
	url(r'^browse/name/(?P<initial>[-\w]+)/$', 
	    views.browse_by_name, name='browse_by_name'),

    url(r'^accounts/password/reset/$', password_reset, 
        {'template_name': 'registration/password_reset_form.html'}, 
        name="password_reset"),
    url(r'^accounts/password/reset/done/$', 
        password_reset_done, 
        {'template_name': 'registration/password_reset_done.html'}, 
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, 
        {'template_name': 'registration/password_reset_confirm.html'}, 
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    
    url(r'^accounts/register/$', 
        MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/create_profile/$', 
        views.create_profile, name='registration_create_profile'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),

]