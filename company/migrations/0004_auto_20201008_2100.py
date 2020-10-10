# Generated by Django 2.2.15 on 2020-10-08 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20201008_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='accounts.Item'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
