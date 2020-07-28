# Generated by Django 3.0.8 on 2020-07-28 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acm_api', '0016_auto_20200728_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocerylist',
            name='items',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='acm_api.CheckList'),
        ),
        migrations.AlterField(
            model_name='grocerylist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
