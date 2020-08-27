from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, ListView
from jedi_academy import settings
from mainapp.forms import PadawanCreationForm, JediCreationForm, AnswerForm, JediChooseForm
from mainapp.models import PadawanModel, JediModel, AnswerModel, JedisPadawan


def send_chose_mail(padawan, jedi):
    """Функция отправки Email"""
    title = f'Поздравляем, {padawan}! Вас выбрал Джедай!'
    message = f'О, какое счастье! Теперь вы сможете учиться у великого Джедая {jedi} на портале "{settings.SITE_NAME}"!'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [padawan.email], fail_silently=False)


class IndexView(TemplateView):
    """Класс рендера стартовой страница"""
    template_name = "index.html"


class PadawanCreateView(CreateView):
    """Класс создания кандидата"""
    template_name = "create_padavan.html"
    model = PadawanModel
    form_class = PadawanCreationForm

    def get_success_url(self):
        return reverse_lazy('main:task', kwargs={'padawan_pk': self.object.pk})


class JediCreateView(CreateView):
    """Класс создания Джедая (для удобства)"""
    template_name = "create_jedi.html"
    model = JediModel
    form_class = JediCreationForm
    success_url = reverse_lazy('main:create_jedi')


class TaskView(FormView):
    """Класс рендера вопросов кандидату"""
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
    """Класс-форма выбора Джедая перед страницей выбора падаванов"""
    template_name = 'chosing_jedi.html'
    model = JediModel
    form_class = JediChooseForm

    def get_success_url(self):
        return reverse_lazy('main:candidates_for_jedi', kwargs={'jedi_pk': self.request.POST['jedi']})


class CandidatesView(ListView):
    """Класс-список кандидатов в падаваны"""
    template_name = 'candidates_list.html'
    model = PadawanModel

    def get_queryset(self):
        planet = get_object_or_404(JediModel, pk=self.kwargs['jedi_pk']).planet_id
        return PadawanModel.objects.filter(planet_id=planet)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jedi_pk'] = self.kwargs['jedi_pk']
        return context


def add_padawan(request, jedi_pk, padawan_pk):
    """Функция добавления кандидата в падаваны с проверками и отправкой поздравительного email"""
    padawan_count = JedisPadawan.objects.filter(jedi_id=jedi_pk, padawan_id=padawan_pk)
    padawan_exists_another_jedi = JedisPadawan.objects.filter(padawan_id=padawan_pk).exclude(jedi_id=jedi_pk)

    if padawan_count and len(padawan_count) < 3:
        # Если этот падаван уже числится учеником у выбранного Джедая:
        msg = {
            'msg': 'Выбранный Вами кандидат уже учится у Вас!',
        }
        return render(request, 'candidates_list.html', msg)
    elif padawan_exists_another_jedi:
        # Если этот падаван уже числится учеником у другого Джедая:
        another_jedi = JedisPadawan.objects.get(padawan_id=padawan_pk).jedi
        msg = {
            'msg': f'Выбранный Вами кандидат уже учится у другого Джедая '
                         f'(у {another_jedi.name} {another_jedi.surname})!',
        }
        return render(request, 'candidates_list.html', msg)
    # условие ">" - для захвата ошибок с "перескоком" числа:
    # чтобы условие ограничения набора не отключилось
    # в случае, если по какой-то причине у Джедая уже будет больше
    # 3 падаванов (например, по личному решению администратора)
    elif len(padawan_count) >= 3:
        msg = {
            'msg': 'Максимальное количество падаванов у одного Джедая - 3. К сожалению, вы уже набрали максимально '
                   'возможное число учеников.',
        }
        return render(request, 'candidates_list.html', msg)

    padawan = PadawanModel.objects.get(id=padawan_pk)
    jedi = JediModel.objects.get(id=jedi_pk)
    msg = {
        'msg': f'Поздравляем! Вы выбрали {padawan}! Да прибудет с Вами сила и терпение!',
    }
    JedisPadawan.objects.create(jedi_id=jedi_pk, padawan_id=padawan_pk)
    send_chose_mail(padawan, jedi)
    return render(request, 'candidates_list.html', msg)
