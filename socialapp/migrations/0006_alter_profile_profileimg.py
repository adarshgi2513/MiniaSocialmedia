# Generated by Django 5.0 on 2023-12-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0005_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='download(2).jfif', upload_to='profile_images'),
        ),
    ]