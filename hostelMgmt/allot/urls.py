from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
import allot.views# import settings
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'allot.views.checktime', name='checktime'),
    url(r'boys', 'allot.views.allotmentform', name='allotmentform'),
    # url(r'^allotment/', include('allot.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
