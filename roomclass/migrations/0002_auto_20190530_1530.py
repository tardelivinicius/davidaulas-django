# Generated by Django 2.2.1 on 2019-05-30 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomclass', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomclass',
            old_name='user',
            new_name='student',
        ),
    ]
