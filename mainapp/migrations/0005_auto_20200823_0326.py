# Generated by Django 3.1 on 2020-08-23 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200823_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='title',
            field=models.CharField(default=0, max_length=32, verbose_name='Название теста'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='questions',
            field=models.ManyToManyField(max_length=128, to='mainapp.QuestionModel', verbose_name='Вопрос задания'),
        ),
    ]
