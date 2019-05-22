# Generated by Django 2.2.1 on 2019-05-22 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190521_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedate',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='date_course',
            field=models.ManyToManyField(related_name='date_course', to='courses.CourseDate'),
        ),
    ]