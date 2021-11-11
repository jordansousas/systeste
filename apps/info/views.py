from django.shortcuts import render

from django.views.generic import(
    TemplateView
)

class InfoView(TemplateView):
    template_name = "info/info.html"

    def get_context_data(self, **kwargs):

            context = super(InfoView, self).get_context_data(**kwargs)

            return context