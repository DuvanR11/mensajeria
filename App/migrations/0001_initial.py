# Generated by Django 4.0.6 on 2022-09-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=25)),
                ('message', models.TextField(max_length=500)),
                ('file', models.FileField(upload_to='foto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Read', 'Read')], default='Pending', max_length=20)),
            ],
        ),
    ]
