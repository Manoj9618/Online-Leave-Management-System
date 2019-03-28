# Generated by Django 2.1 on 2018-11-16 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0021_auto_20181116_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeestatus',
            name='id',
        ),
        migrations.RemoveField(
            model_name='gender',
            name='id',
        ),
        migrations.RemoveField(
            model_name='maritalstatus',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usertype',
            name='id',
        ),
        migrations.AlterField(
            model_name='employeestatus',
            name='employee_status',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='maritalstatus',
            name='marital_status',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='user_type',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]