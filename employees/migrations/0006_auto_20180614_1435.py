# Generated by Django 2.0.6 on 2018-06-14 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_auto_20180608_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['last_name', 'first_name', 'middle_name']},
        ),
    ]