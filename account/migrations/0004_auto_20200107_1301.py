# Generated by Django 2.1 on 2020-01-07 13:01

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
    ]