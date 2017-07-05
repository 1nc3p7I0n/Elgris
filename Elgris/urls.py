from django.conf.urls import patterns, include, url
from main import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^city/(?P<city_name>\w{0,50})/$', views.more_city),
    url(r'^state/(?P<state_name>\w{0,50})/$', views.more_state),
    url(r'^country/(?P<country_name>\w{0,50})/$', views.more_country),
)
