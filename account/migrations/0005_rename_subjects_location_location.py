# Generated by Django 3.2 on 2022-05-04 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220504_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='subjects',
            new_name='location',
        ),
    ]
