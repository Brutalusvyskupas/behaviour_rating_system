# Generated by Django 3.2 on 2021-04-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(default='untitled', max_length=100),
        ),
    ]
