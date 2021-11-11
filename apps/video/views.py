from django.shortcuts import render

from django.views.generic import(
    TemplateView
)

class VideoView(TemplateView):
    template_name = "video/video.html"

    def get_context_data(self, **kwargs):

            context = super(VideoView, self).get_context_data(**kwargs)

            return context