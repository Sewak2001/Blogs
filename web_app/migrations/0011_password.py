# Generated by Django 4.1.6 on 2023-04-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0010_delete_add_delete_file_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=222)),
                ('new_password', models.CharField(max_length=222)),
            ],
        ),
    ]
