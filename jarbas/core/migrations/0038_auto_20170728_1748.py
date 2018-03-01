# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20170727_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalreimbursement',
            name='reimbursement_text',
        ),
        migrations.RemoveField(
            model_name='reimbursement',
            name='reimbursement_text',
        ),
        migrations.AddField(
            model_name='historicalreimbursement',
            name='receipt_text',
            field=models.TextField(blank=True, null=True, verbose_name='Texto do Recibo'),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='receipt_text',
            field=models.TextField(blank=True, null=True, verbose_name='Texto do Recibo'),
        ),
    ]