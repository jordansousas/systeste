from django import urls
from django.urls import path
from .views import BioView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', BioView.as_view(), name='bio')
]