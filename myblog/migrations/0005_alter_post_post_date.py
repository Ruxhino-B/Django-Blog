# Generated by Django 3.2 on 2021-04-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
