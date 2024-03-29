# Generated by Django 4.0.3 on 2023-06-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('specialty', models.CharField(choices=[('Cardiology', 'Cardiology'), ('Dermatology', 'Dermatology'), ('Neurology', 'Neurology'), ('Orthopedics', 'Orthopedics'), ('Pediatrics', 'Pediatrics'), ('Ophthalmology', 'Ophthalmology'), ('Gynecology', 'Gynecology'), ('Urology', 'Urology'), ('Oncology', 'Oncology'), ('Psychiatry', 'Psychiatry'), ('ENT', 'ENT')], max_length=255)),
                ('qualifications', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
