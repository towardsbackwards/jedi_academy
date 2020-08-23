from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from mainapp.forms import PadavanCreationForm, JediCreationForm
from mainapp.models import PadavanModel, JediModel


class IndexView(TemplateView):
    """Generic class for index page rendering"""
    model = ''
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PadavanCreateView(CreateView):
    template_name = "create_padavan.html"
    model = PadavanModel
    form_class = PadavanCreationForm
    success_url = reverse_lazy('main:create_padavan')


class JediCreateView(CreateView):
    template_name = "create_jedi.html"
    model = JediModel
    form_class = JediCreationForm
    success_url = reverse_lazy('main:create_jedi')
