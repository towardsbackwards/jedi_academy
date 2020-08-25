from django.urls import path

from mainapp.views import IndexView, PadawanCreateView, JediCreateView, TaskView

app_name = 'main'

urlpatterns = [
    # ex: /polls/5/
    path('', IndexView.as_view(), name='index'),
    path('create/padawan', PadawanCreateView.as_view(), name='create_padawan'),
    path('create/jedi', JediCreateView.as_view(), name='create_jedi'),
    path('task/', TaskView.as_view(), name='task')
]