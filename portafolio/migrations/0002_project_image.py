# Generated by Django 4.0.1 on 2023-11-23 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='path_to_default_image.jpg', upload_to='portafolio/imagenes'),
        ),
    ]
