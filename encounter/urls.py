from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('encounter.views',
    # Examples:
    url(r'^$', 'index'),
    url(r'^index/$', 'index'),
    url(r'^add/$', 'add'),
    url(r'^add/entity/(\d+)/$', 'add_entity'),
    url(r'^edit/(\d+)/$', 'edit'),
    url(r'^delete/(\d+)/$', 'delete')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
