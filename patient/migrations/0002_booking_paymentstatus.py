# Generated by Django 4.1 on 2023-04-07 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='paymentstatus',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]