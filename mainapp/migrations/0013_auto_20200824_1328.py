# Generated by Django 3.1 on 2020-08-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20200824_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionmodel',
            name='task',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='questions',
            field=models.ManyToManyField(max_length=128, to='mainapp.QuestionModel', verbose_name='Вопрос задания'),
        ),
    ]