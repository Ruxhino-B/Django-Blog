# Generated by Django 3.2 on 2021-04-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_koment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emer', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='katekoria',
            field=models.TextField(default='Django'),
        ),
    ]
