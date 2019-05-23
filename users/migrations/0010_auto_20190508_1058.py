# Generated by Django 2.1.5 on 2019-05-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190508_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('rsc', 'researcher'), ('man', 'manager'), ('adm', 'admin')], default='man', max_length=3),
        ),
    ]
