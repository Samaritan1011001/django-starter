# Generated by Django 3.0.8 on 2020-07-28 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acm_api', '0004_grocerylist_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerylist',
            name='text',
        ),
    ]
