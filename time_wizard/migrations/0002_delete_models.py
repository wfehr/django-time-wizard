# Generated by Django 2.1.9 on 2019-07-06 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_wizard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absoluteperiodmodel',
            name='periodmodel_ptr',
        ),
        migrations.RemoveField(
            model_name='holidayrangeperiodmodel',
            name='periodmodel_ptr',
        ),
        migrations.RemoveField(
            model_name='periodmodel',
            name='container',
        ),
        migrations.RemoveField(
            model_name='periodmodel',
            name='polymorphic_ctype',
        ),
        migrations.DeleteModel(
            name='AbsolutePeriodModel',
        ),
        migrations.DeleteModel(
            name='HolidayRangePeriodModel',
        ),
        migrations.DeleteModel(
            name='PeriodModel',
        ),
        migrations.DeleteModel(
            name='TimeWizardModel',
        ),
    ]
