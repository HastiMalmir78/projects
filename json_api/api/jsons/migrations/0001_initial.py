# Generated by Django 4.1.7 on 2023-04-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('job_url', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_link', models.CharField(max_length=255)),
                ('company_location', models.CharField(max_length=150)),
            ],
        ),
    ]
