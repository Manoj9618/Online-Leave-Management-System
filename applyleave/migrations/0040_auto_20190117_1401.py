# Generated by Django 2.1.5 on 2019-01-17 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0039_auto_20190117_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 14, 1, 3, 841073), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 14, 1, 3, 842073), null=True),
        ),
    ]
