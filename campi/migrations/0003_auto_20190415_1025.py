# Generated by Django 2.1.5 on 2019-04-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campi', '0002_auto_20190415_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='acronym',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='campus',
            name='address',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='campus',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
