# Generated by Django 3.1 on 2020-08-23 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20200823_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jedimodel',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.planetmodel', verbose_name='Планета обучения'),
        ),
        migrations.AlterField(
            model_name='padawanmodel',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.planetmodel', verbose_name='Планета обитания'),
        ),
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=1024, verbose_name='Текст ответа')),
                ('padawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.padawanmodel', verbose_name='Отвчечавший падаван')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.questionmodel', verbose_name='Вопрос')),
            ],
        ),
    ]