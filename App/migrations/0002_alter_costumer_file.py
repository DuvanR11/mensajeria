# Generated by Django 4.0.6 on 2022-09-01 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='file',
            field=models.FileField(upload_to='foto'),
        ),
    ]