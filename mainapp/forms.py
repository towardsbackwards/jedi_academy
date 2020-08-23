from django.forms import ModelForm
from django.urls import reverse_lazy

from mainapp.models import PadavanModel


class PadavanCreationForm(ModelForm):
    form_label = 'Анкета юного падавана'
    button_label = 'Сохранить'

    class Meta:
        model = PadavanModel
        fields = '__all__'

    method = 'POST'
    process_url = reverse_lazy('main:create_padavan')

    def __init__(self, *args, **kwargs):
        super(PadavanCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class JediCreationForm(ModelForm):
    form_label = 'Анкета опытного джедая'
    button_label = 'Сохранить'

    class Meta:
        model = PadavanModel
        fields = '__all__'

    method = 'POST'
    process_url = reverse_lazy('main:create_jedi')

    def __init__(self, *args, **kwargs):
        super(JediCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'