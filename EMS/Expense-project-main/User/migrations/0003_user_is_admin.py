# Generated by Django 4.1.7 on 2023-03-21 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, null=True),
        ),
    ]