# Generated by Django 2.0 on 2019-10-10 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0029_auto_20191010_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='classroom',
        ),
    ]
