# Generated by Django 4.1.6 on 2023-03-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tittle',
            field=models.CharField(default=2, max_length=222),
            preserve_default=False,
        ),
    ]
