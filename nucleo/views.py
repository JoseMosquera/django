from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "nucleo/home.html"

    def get(self, request, *ars, **kwargs):
        return render(request, self.template_name, {'title':"Mi web"})

class SamplePageView(TemplateView):
    template_name = 'nucleo/sample.html'