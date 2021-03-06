# Generated by Django 2.2.1 on 2019-05-19 19:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0003_auto_20190519_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtInc', models.DateTimeField(default=django.utils.timezone.now)),
                ('protocol', models.CharField(max_length=250)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.IntegerField(choices=[(1, 'Pago'), (2, 'Pendente'), (3, 'Cancelado')], default=2, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='PayMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('status', models.IntegerField(choices=[(1, 'Ativo'), (2, 'Inativo'), (3, 'Deletado')], default=1, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='FinanceControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, 'Pago'), (2, 'Pendente'), (3, 'Cancelado')], default=2, verbose_name='Status')),
                ('finance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='control_finance', to='finances.Finance')),
            ],
        ),
        migrations.AddField(
            model_name='finance',
            name='pay_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finance_paymethods', to='finances.PayMethods'),
        ),
        migrations.AddField(
            model_name='finance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finance_student', to='student.Student'),
        ),
    ]
