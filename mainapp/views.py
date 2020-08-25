from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView
from mainapp.forms import PadawanCreationForm, JediCreationForm, AnswerForm
from mainapp.models import PadawanModel, JediModel, TaskModel, AnswerModel


class IndexView(TemplateView):
    template_name = "index.html"


class PadawanCreateView(CreateView):
    template_name = "create_padavan.html"
    model = PadawanModel
    form_class = PadawanCreationForm
    success_url = reverse_lazy('main:task')


class JediCreateView(CreateView):
    template_name = "create_jedi.html"
    model = JediModel
    form_class = JediCreationForm
    success_url = reverse_lazy('main:create_jedi')


class TaskView(FormView):
    template_name = 'task.html'
    model = AnswerModel
    form_class = AnswerForm
    success_url = reverse_lazy('main:index')
