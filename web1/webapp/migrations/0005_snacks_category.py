# Generated by Django 4.0.5 on 2022-08-14 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_category_rename_snack_name_snacks_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='snacks',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.category'),
        ),
    ]
