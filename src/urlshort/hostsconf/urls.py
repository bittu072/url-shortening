from django.conf.urls import url

from .views

urlpatterns = [
    url(r'^(?P<path>.*)', admin.site.urls),
]
