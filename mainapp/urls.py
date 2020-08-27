from django.urls import path

from mainapp.views import IndexView, PadawanCreateView, JediCreateView, TaskView, ChooseJediView, CandidatesView, \
    add_padawan, JediListView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jedi_list/', JediListView.as_view(), name='jedi_list'),
    path('create/padawan', PadawanCreateView.as_view(), name='create_padawan'),
    path('create/jedi', JediCreateView.as_view(), name='create_jedi'),
    path('task/<int:padawan_pk>', TaskView.as_view(), name='task'),
    path('choose/', ChooseJediView.as_view(), name='choose_jedi'),
    path('choose/padawan_candidates/<int:jedi_pk>', CandidatesView.as_view(), name='candidates_for_jedi'),
    path('choose/padawan_candidates/<int:jedi_pk>/<int:padawan_pk>', add_padawan, name='take_padawan')
]