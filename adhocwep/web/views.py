from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView

from web.forms import contactform
from web.models import *
from django.contrib import messages
# Create your views here.

class contactcreateView(CreateView):
    model=contact
    form_class=contactform
    template_name="index.html"
    success_url=reverse_lazy('webpaguina')

    def post(self, request, *args, **kwargs):
        form = contactform(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            messages.success(self.request, "Gracias por contactarnos")
            return HttpResponseRedirect('#contact')
        return render(request, 'index.html', {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios'] = servicios.objects.filter(estado=True)
        context['portafolios'] = portafolio.objects.filter(estado=True)
        context['about'] = about.objects.filter(estado=True)
        context['feature'] = feature.objects.filter(estado=True)
        return context