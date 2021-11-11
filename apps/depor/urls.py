from django import urls
from django.urls import path
from .views import DeporView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', DeporView.as_view(), name='depor')
]