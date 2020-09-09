# Generated by Django 2.2.15 on 2020-09-09 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ブランド')),
                ('item_model', models.CharField(max_length=50, verbose_name='モデル名')),
                ('category', models.CharField(choices=[('shirt', 'シャツ'), ('pant', 'パンツ'), ('Tshirt', 'Tシャツ')], max_length=20)),
                ('condition', models.CharField(choices=[('s', 'S'), ('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=1)),
                ('text', models.TextField(verbose_name='備考')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to='', verbose_name='添付画像')),
                ('target', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Item', verbose_name='アイテム')),
            ],
        ),
    ]
