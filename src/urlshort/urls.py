from django.conf.urls import url
from django.contrib import admin

# from goshort.views import goshort_redirect_view

from goshort.views import goshortCBview, GoShortView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', GoShortView.as_view()),
    url(r'^a/(?P<shorturl>[\w-]+)/$', goshortCBview.as_view()),
]


# update following line in settings file
# ALLOWED_HOSTS = ['www.trialshort.com']
