# Generated by Django 3.1 on 2020-08-26 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20200825_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='JedisPadawan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jedi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.jedimodel', verbose_name='Джедай')),
            ],
        ),
    ]
