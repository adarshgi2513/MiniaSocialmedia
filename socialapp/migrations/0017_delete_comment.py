# Generated by Django 5.0 on 2023-12-13 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0016_alter_comment_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
