# Generated by Django 2.0 on 2019-10-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0032_text_classroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miner',
            name='classroom',
            field=models.ManyToManyField(blank=True, related_name='participants', to='mine.Classroom'),
        ),
    ]
