# Generated by Django 4.0.5 on 2022-08-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_remove_snacks_views_delete_ip_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snacks',
            name='image',
            field=models.ImageField(upload_to='web1/dbimages/'),
        ),
    ]
