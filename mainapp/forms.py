from django import forms
from django.forms import ModelForm, BaseModelFormSet, modelformset_factory, BaseFormSet

from django.urls import reverse_lazy

from mainapp.models import PadawanModel, JediModel, TaskModel, AnswerModel, QuestionModel


class PadawanCreationForm(ModelForm):
    form_label = 'Анкета юного падавана'
    button_label = 'Далее'

    class Meta:
        model = PadawanModel
        fields = '__all__'


    method = 'POST'
    # process_url (form action=) - куда отправляются post-данные
    process_url = reverse_lazy('main:create_padawan')

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


# class TaskForm(ModelForm):
#     form_label = 'Тестовое задание на падавана'
#     button_label = 'Отправить ответы'
#
#     class Meta:
#         model = TaskModel
#         fields = '__all__'
#         exclude = ['title', 'unique_code']
#
#     method = 'POST'
#     process_url = reverse_lazy('main:create_padawan')
#
#     def __init__(self, *args, **kwargs):
#         super(TaskForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'


class AnswerForm(forms.Form):

    form_label = 'Тестовое задание на падавана'
    button_label = 'Отправить ответы'
    method = 'POST'
    process_url = reverse_lazy('main:index')

    def __init__(self, *args, **kwargs):
        """KWARGS ТУТ!
        name
        surname
        age
        planet
        email"""
        super(AnswerForm, self).__init__(*args, **kwargs)
        questions = QuestionModel.objects.all()
        print(kwargs)
        for question in questions:
            self.fields[question.title] = forms.CharField(label=question.question, required=False)
            self.fields[question.title].widget.attrs['class'] = 'form-control'
