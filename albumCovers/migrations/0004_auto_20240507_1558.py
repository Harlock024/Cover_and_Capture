# Generated by Django 2.1.4 on 2024-05-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albumCovers', '0003_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumcover',
            name='cover_url',
            field=models.URLField(),
        ),
    ]