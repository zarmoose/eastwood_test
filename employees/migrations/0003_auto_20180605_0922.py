# Generated by Django 2.0.6 on 2018-06-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20180605_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='end_work',
            field=models.DateField(blank=True, null=True),
        ),
    ]