# Generated by Django 5.0.4 on 2024-04-16 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='expense',
            name='category',
        ),
        migrations.RemoveField(
            model_name='income',
            name='category',
        ),
        migrations.AddField(
            model_name='expense',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cashflow.category'),
        ),
        migrations.AddField(
            model_name='income',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cashflow.category'),
        ),
    ]