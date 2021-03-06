# Generated by Django 2.1 on 2018-11-26 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0027_auto_20181126_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveApplicationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=50)),
                ('tenure_month', models.IntegerField(default=0)),
                ('applied_on', models.DateTimeField(default=datetime.datetime(2018, 11, 26, 17, 44, 55, 676084), null=True)),
                ('leave_month', models.DateField()),
                ('leave_type', models.CharField(max_length=50)),
                ('leave_start', models.DateField()),
                ('leave_end', models.DateField()),
                ('leave_for', models.CharField(max_length=10)),
                ('days', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('reason', models.CharField(max_length=100, null=True)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('DELETED', 'DELETED'), ('CANCELLED', 'CANCELLED')], max_length=50, null=True)),
                ('log_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 26, 17, 44, 55, 674084), null=True),
        ),
    ]
