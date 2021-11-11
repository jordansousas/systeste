
from django.contrib import admin
from django.urls import path, include

from apps.home import urls as home_urls
from apps.info import urls as info_urls
from apps.depor import urls as depor_urls
from apps.video import urls as video_urls
from apps.sobre import urls as sobre_urls
from apps.bio import urls as bio_urls

urlpatterns = [
    path('', include(home_urls)),
    path('info/', include(info_urls)),
    path('depor/', include(depor_urls)),
    path('video/', include(video_urls)),
    path('sobre/', include(sobre_urls)),
    path('bio/', include(bio_urls)),
]
