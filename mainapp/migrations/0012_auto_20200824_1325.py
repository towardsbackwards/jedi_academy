# Generated by Django 3.1 on 2020-08-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20200824_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='question',
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='task',
            field=models.ManyToManyField(max_length=128, to='mainapp.TaskModel', verbose_name='Вопрос задания'),
        ),
    ]
