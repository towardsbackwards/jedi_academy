from django.contrib import admin
from .models import PlanetModel, QuestionModel, TaskModel, PadawanModel, JediModel, AnswerModel

admin.site.register(PlanetModel)
admin.site.register(QuestionModel)
admin.site.register(TaskModel)
admin.site.register(PadawanModel)
admin.site.register(JediModel)
admin.site.register(AnswerModel)