# Generated by Django 2.2.10 on 2020-06-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200620_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='student', to='school.Teacher'),
        ),
    ]
