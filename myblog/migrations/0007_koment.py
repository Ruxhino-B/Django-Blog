# Generated by Django 3.2 on 2021-04-25 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0006_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_komenti', models.DateTimeField(auto_now_add=True)),
                ('komentues', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='koment_user', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='koment_post', to='myblog.post')),
            ],
        ),
    ]
