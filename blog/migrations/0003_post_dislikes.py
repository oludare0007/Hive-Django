# Generated by Django 5.0.1 on 2024-01-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Dislikes',
            field=models.IntegerField(default=0),
        ),
    ]
