# Generated by Django 4.0.4 on 2022-05-02 19:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_post', models.CharField(max_length=255)),
                ('data_post', models.DateTimeField(default=datetime.datetime(2022, 5, 2, 19, 12, 47, 916143, tzinfo=utc))),
                ('conteudo_post', models.TextField()),
                ('imagem_post', models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d')),
                ('publicado_post', models.BooleanField(default=False)),
                ('autor_post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('categoria_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria')),
            ],
        ),
    ]
