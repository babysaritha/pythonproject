# Generated by Django 4.0.5 on 2022-07-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-07-11'),
            preserve_default=False,
        ),
    ]