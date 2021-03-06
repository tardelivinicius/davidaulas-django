# Generated by Django 2.2.1 on 2019-05-19 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finance',
            options={'verbose_name': 'finance', 'verbose_name_plural': 'finance'},
        ),
        migrations.AlterModelOptions(
            name='financecontrol',
            options={'verbose_name': 'financecontrol', 'verbose_name_plural': 'financescontrol'},
        ),
        migrations.AlterModelOptions(
            name='paymethods',
            options={'verbose_name': 'PayMethod', 'verbose_name_plural': 'paymethods'},
        ),
        migrations.AlterModelTable(
            name='finance',
            table='finances',
        ),
        migrations.AlterModelTable(
            name='financecontrol',
            table='finances_control',
        ),
        migrations.AlterModelTable(
            name='paymethods',
            table='finances_paymethods',
        ),
    ]
