# Generated by Django 3.0.8 on 2020-07-28 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acm_api', '0018_auto_20200728_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerylist',
            name='items',
        ),
    ]
