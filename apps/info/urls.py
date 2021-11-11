from django import urls
from django.urls import path
from .views import InfoView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', InfoView.as_view(), name='info')
]