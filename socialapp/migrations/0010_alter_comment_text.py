# Generated by Django 5.0 on 2023-12-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=50),
        ),
    ]