# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-31 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0008_auto_20171231_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.Topping'),
        ),
    ]