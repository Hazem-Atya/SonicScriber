# Generated by Django 4.2.7 on 2023-11-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='transcription',
            field=models.TextField(null=True),
        ),
    ]
