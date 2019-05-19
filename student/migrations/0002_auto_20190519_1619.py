# Generated by Django 2.2.1 on 2019-05-19 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Number',
            new_name='Phone',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'address', 'verbose_name_plural': 'adresses'},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name': 'phone', 'verbose_name_plural': 'phones'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
        migrations.AlterModelTable(
            name='address',
            table='adresses',
        ),
        migrations.AlterModelTable(
            name='phone',
            table='phones',
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
    ]
