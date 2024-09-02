# Generated by Django 5.1 on 2024-09-02 17:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('profile_summary', models.CharField(blank=True, max_length=255, null=True)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('year_of_passout', models.DateField(blank=True, null=True)),
                ('previous_employment', models.CharField(blank=True, max_length=255, null=True)),
                ('projects', models.CharField(max_length=255, null=True)),
                ('certification', models.CharField(blank=True, max_length=255, null=True)),
                ('skills', models.CharField(blank=True, max_length=255, null=True)),
                ('socials', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Prefer not to say', 'Prefer not to say')], default='Prefer not to say', max_length=30)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_candidate',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiring_for', models.CharField(choices=[('Company', 'Company'), ('individual', 'individual')], default='Company', max_length=30)),
                ('pan_number', models.CharField(blank=True, max_length=10, null=True)),
                ('official_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('company_address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_employer',
                'managed': True,
            },
        ),
    ]
