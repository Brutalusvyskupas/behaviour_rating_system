# Generated by Django 3.2 on 2022-04-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userworkoffice_office_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='profile_pics/profile.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='userworkoffice',
            name='office_image',
            field=models.ImageField(default='office.jpg', upload_to='office_pics'),
        ),
    ]
