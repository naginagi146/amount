# Generated by Django 2.2.15 on 2020-09-11 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
