# Generated by Django 2.0.6 on 2018-06-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='end_work',
            field=models.DateField(blank=True),
        ),
    ]
