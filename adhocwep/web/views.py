from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from web.models import *
# Create your views here.

class weblistView(ListView):
    model = servicios
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios'] = servicios.objects.filter(estado=True)
        context['portafolios'] = portafolio.objects.filter(estado=True)
        context['about'] = about.objects.filter(estado=True)
        context['feature'] = feature.objects.filter(estado=True)
        return context
