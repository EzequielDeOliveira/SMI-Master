# Generated by Django 3.0.2 on 2020-03-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('transductors', '0015_auto_20200217_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='energytransductor',
            name='history',
            field=models.TextField(blank=True, verbose_name='history'),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='grouping',
            field=models.ManyToManyField(help_text='This field is required', to='groups.Group', verbose_name='grouping'),
        ),
    ]
