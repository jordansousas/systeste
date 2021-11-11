from django.shortcuts import render

from django.views.generic import(
    TemplateView
)

class BioView(TemplateView):
    template_name = "bio/bio.html"

    def get_context_data(self, **kwargs):

            context = super(BioView, self).get_context_data(**kwargs)

            return context