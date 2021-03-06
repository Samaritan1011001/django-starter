# Generated by Django 3.0.8 on 2020-07-30 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=50)),
                ('completed', models.BooleanField(default=False)),
                ('items', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='acm_api.GroceryList')),
            ],
        ),
    ]
