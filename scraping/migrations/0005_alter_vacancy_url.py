# Generated by Django 5.0.1 on 2024-02-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_alter_vacancy_options_alter_vacancy_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
