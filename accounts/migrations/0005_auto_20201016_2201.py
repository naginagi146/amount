# Generated by Django 2.2.15 on 2020-10-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_item_contributor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(upload_to='media/', verbose_name='添付画像'),
        ),
    ]
