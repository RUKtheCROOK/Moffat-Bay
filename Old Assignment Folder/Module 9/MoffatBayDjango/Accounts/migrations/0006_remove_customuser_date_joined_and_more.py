# Generated by Django 5.1 on 2024-09-08 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_customuser_date_joined_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
