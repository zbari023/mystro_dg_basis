# Generated by Django 4.2.2 on 2023-06-14 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_mypost_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='image',
            field=models.ImageField(default='', upload_to='autor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mypost',
            name='image',
            field=models.ImageField(default='', upload_to='post'),
            preserve_default=False,
        ),
    ]