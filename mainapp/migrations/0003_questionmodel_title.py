# Generated by Django 3.1 on 2020-08-22 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200823_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionmodel',
            name='title',
            field=models.CharField(default=0, max_length=32, verbose_name='Название планеты'),
            preserve_default=False,
        ),
    ]
