# Generated by Django 4.0.6 on 2022-09-02 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='costumer',
            old_name='status',
            new_name='estado',
        ),
    ]