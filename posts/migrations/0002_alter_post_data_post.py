# Generated by Django 4.0.4 on 2022-05-02 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
