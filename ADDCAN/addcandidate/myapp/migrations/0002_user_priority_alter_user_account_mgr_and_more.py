# Generated by Django 4.2.7 on 2023-12-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='priority',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_mgr',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='budget_max',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='budget_min',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='exp_range_min',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='good_to_have',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='max',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='must_have',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='positions',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='recruiter',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='skillsets',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='title_for_req',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='work_type',
            field=models.CharField(max_length=25),
        ),
    ]
