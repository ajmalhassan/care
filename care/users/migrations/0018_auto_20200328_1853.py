# Generated by Django 2.2.11 on 2020-03-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0017_auto_20200328_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(5, 'Doctor'), (10, 'Staff'), (15, 'Patient'), (20, 'Volunteer'),
                                               (25, 'DistrictNodalLabOfficer'), (30, 'DistrictAdmin')]),
        ),
    ]
