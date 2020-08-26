from django import forms
from django.forms import ModelForm, BaseModelFormSet, modelformset_factory, BaseFormSet

from django.urls import reverse_lazy

from mainapp.models import PadawanModel, JediModel, TaskModel, AnswerModel, QuestionModel, JedisPadawan


class PadawanCreationForm(ModelForm):
    form_label = 'Анкета юного падавана'
    button_label = 'Далее'
    method = 'POST'
    process_url = reverse_lazy('main:create_padawan')  # - куда отправляются post-данные

    class Meta:
        model = PadawanModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PadawanCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class JediCreationForm(ModelForm):
    form_label = 'Анкета опытного джедая'
    button_label = 'Сохранить'

    class Meta:
        model = JediModel
        fields = '__all__'

    method = 'POST'
    process_url = reverse_lazy('main:create_jedi')

    def __init__(self, *args, **kwargs):
        super(JediCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AnswerForm(forms.Form):
    form_label = 'Тестовое задание на падавана'
    button_label = 'Отправить ответы'
    method = 'POST'

    def __init__(self, *args, **kwargs):
        questions = QuestionModel.objects.all()
        self.padawan_pk = kwargs.pop('padawan_pk', None)
        super(AnswerForm, self).__init__(*args, **kwargs)
        for question in questions:
            self.fields[question.title] = forms.CharField(label=question.question, required=False)
            self.fields[question.title].widget.attrs['class'] = 'form-control'

    def save(self):
        for k, v in self.cleaned_data.items():
            AnswerModel.objects.create(question=QuestionModel.objects.get(title=k),
                                       padawan=PadawanModel.objects.get(id=self.padawan_pk), answer=v)


class JediChooseForm(ModelForm):
    form_label = 'Выберите себя'
    button_label = 'Далее'

    class Meta:
        model = JedisPadawan
        fields = '__all__'

    method = 'POST'
    process_url = reverse_lazy('main:choose_jedi')

    def __init__(self, *args, **kwargs):
        super(JediChooseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'