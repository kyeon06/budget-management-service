# Generated by Django 4.2.7 on 2023-11-16 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure',
            name='comment',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='지출메모'),
        ),
    ]
