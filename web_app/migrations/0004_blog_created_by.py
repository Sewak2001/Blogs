# Generated by Django 4.1.6 on 2023-03-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_by',
            field=models.CharField(default=2, max_length=222),
            preserve_default=False,
        ),
    ]