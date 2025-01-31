# Generated by Django 5.1.3 on 2024-11-18 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('batch_number', models.CharField(max_length=50)),
                ('expiration_date', models.DateField()),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StockLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('in', 'Load'), ('out', 'Offload')], max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.drug')),
            ],
        ),
    ]
