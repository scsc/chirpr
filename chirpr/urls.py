from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include
from django.core.urlresolvers import reverse_lazy

import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chirpr_project.views.home', name='home'),
    # url(r'^chirpr_project/', include('chirpr_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),


    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('index')},
        name='auth_logout'),

    url(r'^accounts/profile/$',
        views.RedirectToIndex.as_view(),
        name='auth_profile'),

    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^$', views.index, name='index'),

    url(r'^chirp/$', views.chirp, name="chirp"),
)

