# Generated by Django 2.2.5 on 2019-10-17 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20190519_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='dtInc',
            new_name='date_joined',
        ),
    ]