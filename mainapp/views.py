from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, ListView
from mainapp.forms import PadawanCreationForm, JediCreationForm, AnswerForm, JediChooseForm
from mainapp.models import PadawanModel, JediModel, AnswerModel, PlanetModel


class IndexView(TemplateView):
    template_name = "index.html"


class PadawanCreateView(CreateView):
    template_name = "create_padavan.html"
    model = PadawanModel
    form_class = PadawanCreationForm

    def get_success_url(self):
        return reverse_lazy('main:task', kwargs={'padawan_pk': self.object.pk})


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

    def get_form_kwargs(self):
        padawan_pk = self.kwargs.get('padawan_pk', None)
        form_kwargs = super(TaskView, self).get_form_kwargs()
        form_kwargs['padawan_pk'] = padawan_pk
        return form_kwargs

    def form_valid(self, form):
        form.save()
        return super(TaskView, self).form_valid(form)


class ChooseJediView(FormView):
    template_name = 'list.html'
    model = JediModel
    form_class = JediChooseForm

    def get_success_url(self):
        return reverse_lazy('main:candidates_for_jedi', kwargs={'jedi_pk': self.request.POST['jedi']})


class CandidatesView(ListView):
    template_name = 'list2.html'
    model = PadawanModel

    def get_queryset(self):
        planet = get_object_or_404(JediModel, pk=self.kwargs['jedi_pk']).planet_id
        return PadawanModel.objects.filter(planet_id=planet)

