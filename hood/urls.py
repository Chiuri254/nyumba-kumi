from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import RedirectView

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/',views.search_category,name='search_category'),
    url(r'^location/(\d+)',views.display_location,name='displayLocation'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
