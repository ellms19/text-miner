# Generated by Django 2.0 on 2019-09-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0003_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_level',
            field=models.CharField(choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], default='BEGINNER', max_length=12),
        ),
    ]
