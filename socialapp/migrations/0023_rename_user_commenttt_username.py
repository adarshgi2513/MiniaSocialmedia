# Generated by Django 5.0 on 2023-12-18 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0022_rename_user_name_commenttt_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commenttt',
            old_name='user',
            new_name='username',
        ),
    ]
