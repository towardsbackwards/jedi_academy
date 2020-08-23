from django.urls import path

from mainapp.views import IndexView, PadavanCreateView, JediCreateView

app_name = 'main'

urlpatterns = [
    # ex: /polls/5/
    path('', IndexView.as_view(), name='index'),
    path('create/padavan', PadavanCreateView.as_view(), name='create_padavan'),
    path('create/jedi', JediCreateView.as_view(), name='create_jedi')
]