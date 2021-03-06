# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-10 12:57
from __future__ import unicode_literals

import django.db.models.deletion
import time_wizard.workarounds
from django.db import migrations, models
from time_wizard.conf import TIME_WIZARD_COUNTRIES


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodModel',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TimeWizardModel',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AbsolutePeriodModel',
            fields=[
                ('periodmodel_ptr', models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    serialize=False,
                    to='time_wizard.PeriodModel')),
                ('start', models.DateTimeField(
                    blank=True,
                    null=True)),
                ('end', models.DateTimeField(
                    blank=True,
                    null=True)),
            ],
            bases=('time_wizard.periodmodel',),
        ),
        migrations.CreateModel(
            name='HolidayRangePeriodModel',
            fields=[
                ('periodmodel_ptr', models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    serialize=False,
                    to='time_wizard.PeriodModel')),
                ('time_value', models.PositiveSmallIntegerField(
                    default=0,
                    help_text='Amount of time between this and the selected '
                              'holiday.')),
                ('time_unit', models.CharField(
                    blank=True,
                    choices=[
                        ('1', 'Minute'),
                        ('60', 'Hour'),
                        ('1440', 'Day'),
                        ('10080', 'Week')],
                    help_text='Unit for the chosen time_value.',
                    max_length=16)),
                ('range_position', models.CharField(
                    blank=True,
                    choices=[
                        ('before', 'Before'),
                        ('after', 'After'),
                        ('both', 'Both')],
                    help_text='Choose if a given time range is either before, '
                              'after or before and after the selected '
                              'holiday.',
                    max_length=8)),
                ('start_time', models.TimeField(
                    blank=True,
                    null=True)),
                ('end_time', models.TimeField(
                    blank=True,
                    null=True)),
                ('country', models.CharField(
                    choices=[(c, c) for c in TIME_WIZARD_COUNTRIES],
                    max_length=8)),
                ('province', models.CharField(
                    blank=True,
                    max_length=8)),
                ('holiday', models.CharField(
                    max_length=64)),
            ],
            bases=('time_wizard.periodmodel',),
        ),
        migrations.AddField(
            model_name='periodmodel',
            name='container',
            field=models.ForeignKey(
                    on_delete=time_wizard.workarounds.NON_POLYMORPHIC_CASCADE,
                    related_name='periods',
                    to='time_wizard.TimeWizardModel'),
        ),
        migrations.AddField(
            model_name='periodmodel',
            name='polymorphic_ctype',
            field=models.ForeignKey(
                    editable=False,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='polymorphic_time_wizard.periodmodel_set+',
                    to='contenttypes.ContentType'),
        ),
    ]
