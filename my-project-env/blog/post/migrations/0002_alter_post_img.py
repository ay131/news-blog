# Generated by Django 4.0.4 on 2022-05-24 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='download.png', upload_to='post_img/'),
        ),
    ]
