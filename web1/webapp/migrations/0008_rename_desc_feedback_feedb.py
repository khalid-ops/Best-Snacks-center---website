# Generated by Django 4.0.5 on 2022-08-15 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='desc',
            new_name='feedb',
        ),
    ]
