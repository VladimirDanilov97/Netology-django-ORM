# Generated by Django 4.0.1 on 2022-06-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
