# Generated by Django 4.1.5 on 2023-01-25 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('hms_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.BigIntegerField()),
                ('age', models.IntegerField()),
                ('reference_no', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=10)),
                ('booking_date', models.CharField(max_length=20)),
                ('status', models.CharField(default='booked', max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_admin.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.patient')),
            ],
            options={
                'db_table': 'booking_tb',
            },
        ),
        migrations.CreateModel(
            name='Presciption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=20)),
                ('days', models.IntegerField()),
                ('prescription_notes', models.CharField(max_length=100)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.booking')),
            ],
            options={
                'db_table': 'prescription_tb',
            },
        ),
    ]