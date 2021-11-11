from django.shortcuts import render

from django.views.generic import(
    TemplateView
)

class DeporView(TemplateView):
    template_name = "depor/depor.html"

    def get_context_data(self, **kwargs):

            context = super(DeporView, self).get_context_data(**kwargs)

            return context