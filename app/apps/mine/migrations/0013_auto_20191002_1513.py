# Generated by Django 2.0 on 2019-10-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0012_auto_20191002_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='mine.Task'),
        ),
    ]