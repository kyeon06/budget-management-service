# Generated by Django 4.2.7 on 2023-11-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='계정명')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자여부')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser 여부')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]