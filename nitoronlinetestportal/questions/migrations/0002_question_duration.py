# Generated by Django 3.1.7 on 2023-07-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='duration',
            field=models.DurationField(null=True),
        ),
    ]
