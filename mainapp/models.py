from django.db import models
from django.utils.translation import gettext_lazy as _


class PlanetModel(models.Model):
    """Модель планеты"""

    class Meta:
        verbose_name = _("Планета")
        verbose_name_plural = _("Планеты")

    name = models.CharField(_('Название планеты'), max_length=128)

    def __str__(self):
        return self.name


class TaskModel(models.Model):
    """Модель задания"""

    class Meta:
        verbose_name = _("Задание")
        verbose_name_plural = _("Задания")

    title = models.CharField(_('Название теста'), max_length=32)
    unique_code = models.CharField(_('Уникальный код'), max_length=2)


class QuestionModel(models.Model):
    """Модель вопроса к заданию"""

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")

    title = models.CharField(_('Кратское название вопроса'), max_length=32)
    question = models.TextField(_('Текст вопроса'), max_length=128)
    task = models.ForeignKey(TaskModel, verbose_name=_('Вопрос задания'), max_length=128, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PadawanModel(models.Model):
    """Модель кандидата в Падаваны"""

    class Meta:
        verbose_name = _("Кандидат")
        verbose_name_plural = _("Кандидаты")

    name = models.CharField(_('Имя'), max_length=32, blank=False, null=False)
    surname = models.CharField(_('Фамилия'), max_length=128, blank=False, null=False)
    age = models.PositiveIntegerField(_('Возраст'), default=100, blank=False, null=False)
    planet = models.ForeignKey(PlanetModel, verbose_name=_('Планета обитания'),
                               on_delete=models.CASCADE, blank=False, null=False)
    email = models.EmailField(_('E-mail'), max_length=256, blank=False, null=False)

    def __str__(self):
        return f'{self.name} {self.surname}'


class JediModel(models.Model):
    """Модель Джедая"""

    class Meta:
        verbose_name = _("Джедай")
        verbose_name_plural = _("Джедаи")

    name = models.CharField(_('Имя'), max_length=32, blank=False, null=False)
    surname = models.CharField(_('Фамилия'), max_length=128, blank=False, null=False)
    age = models.PositiveIntegerField(_('Возраст'), default=200, blank=False, null=False)
    planet = models.ForeignKey(PlanetModel, verbose_name=_('Планета обучения'),
                               on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.name} {self.surname}'


class AnswerModel(models.Model):
    """Модель ответа падавана"""
    question = models.ForeignKey(QuestionModel, verbose_name=_('Вопрос'),
                                 on_delete=models.CASCADE, blank=False, null=False)
    answer = models.TextField(_('Текст ответа'), max_length=1024, blank=False, null=False)
    padawan = models.ForeignKey(PadawanModel, verbose_name=_('Отвечавший падаван'),
                                on_delete=models.CASCADE, blank=False, null=False)


class JedisPadawan(models.Model):
    jedi = models.ForeignKey(JediModel, verbose_name=_('Джедай'),
                             on_delete=models.CASCADE, blank=True, null=True)
    padawan = models.ForeignKey(PadawanModel, verbose_name=_('Падаван джедая'),
                                on_delete=models.CASCADE, blank=True, null=True)
