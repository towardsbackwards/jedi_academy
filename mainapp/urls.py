from django.urls import path

from mainapp.views import IndexView, PadawanCreateView, JediCreateView, TaskView, ChooseJediView, CandidatesView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/padawan', PadawanCreateView.as_view(), name='create_padawan'),
    path('create/jedi', JediCreateView.as_view(), name='create_jedi'),
    path('task/<int:padawan_pk>', TaskView.as_view(), name='task'),
    path('choose/', ChooseJediView.as_view(), name='choose_jedi'),
    path('choose/padawan_candidates/<int:jedi_pk>', CandidatesView.as_view(), name='candidates_for_jedi')
]