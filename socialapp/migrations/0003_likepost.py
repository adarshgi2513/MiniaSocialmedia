# Generated by Django 5.0 on 2023-12-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='likepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
