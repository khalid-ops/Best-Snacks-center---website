# Generated by Django 4.0.5 on 2022-08-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_name_snacks_snack_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='snacks',
            old_name='snack_name',
            new_name='name',
        ),
    ]
