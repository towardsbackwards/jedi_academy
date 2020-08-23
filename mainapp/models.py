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


class QuestionModel(models.Model):
    """Модель вопроса к заданию"""
    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")

    title = models.CharField(_('Название планеты'), max_length=32)
    text = models.TextField(_('Текст вопроса'), max_length=128)

    def __str__(self):
        return self.title


class TaskModel(models.Model):
    """Модель задания"""
    class Meta:
        verbose_name = _("Задание")
        verbose_name_plural = _("Задания")

    title = models.CharField(_('Название теста'), max_length=32)
    unique_code = models.CharField(_('Уникальный код'), max_length=2)
    questions = models.ManyToManyField(QuestionModel, verbose_name=_('Вопрос задания'), max_length=128)

    def __str__(self):
        return self.title


class PadavanModel(models.Model):
    """Модель кандидата в Джедаи"""
    class Meta:
        verbose_name = _("Кандидат")
        verbose_name_plural = _("Кандидаты")

    name = models.CharField(_('Имя падавана'), max_length=32)
    surname = models.CharField(_('Фамилия падавана'), max_length=128)
    age = models.PositiveIntegerField(_('Возраст падавана'), default=100)
    planet = models.ForeignKey(PlanetModel, verbose_name=_('Планета обитания'),
                               max_length=128, on_delete=models.CASCADE)
    email = models.EmailField(_('Е-мейл'), max_length=256)

    def __str__(self):
        return f'{self.name} {self.surname}'


class JediModel(models.Model):
    """Модель кандидата в Джедаи"""
    class Meta:
        verbose_name = _("Джедай")
        verbose_name_plural = _("Джедаи")

    name = models.CharField(_('Имя джедая'), max_length=32)
    surname = models.CharField(_('Фамилия джедая'), max_length=128)
    age = models.PositiveIntegerField(_('Возраст падавана'), default=200)
    planet = models.ForeignKey(PlanetModel, verbose_name=_('Планета обучения'),
                               max_length=128, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'


