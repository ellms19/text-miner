# Generated by Django 2.0 on 2019-10-04 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0018_auto_20191004_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mine.Classroom'),
        ),
    ]