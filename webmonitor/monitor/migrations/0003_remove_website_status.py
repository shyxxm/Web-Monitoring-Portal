# Generated by Django 4.0.5 on 2022-07-05 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_website_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='status',
        ),
    ]
