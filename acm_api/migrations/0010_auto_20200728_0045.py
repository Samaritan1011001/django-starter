# Generated by Django 3.0.8 on 2020-07-28 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acm_api', '0009_auto_20200728_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acm_api.CheckList'),
        ),
    ]
