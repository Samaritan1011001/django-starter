# Generated by Django 3.0.8 on 2020-07-28 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acm_api', '0008_auto_20200728_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerylist',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='grocerylist',
            name='text',
        ),
    ]