# Generated by Django 2.2.1 on 2019-05-19 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190519_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_student', to='student.Student'),
        ),
    ]