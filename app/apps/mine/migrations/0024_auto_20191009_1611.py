# Generated by Django 2.0 on 2019-10-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0023_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
