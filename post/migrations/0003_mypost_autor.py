# Generated by Django 4.2.2 on 2023-06-14 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mypost_Autor', to='post.autor'),
            preserve_default=False,
        ),
    ]
