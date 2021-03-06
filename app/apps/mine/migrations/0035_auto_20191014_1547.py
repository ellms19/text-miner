# Generated by Django 2.0 on 2019-10-14 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0034_auto_20191014_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderatedtext',
            name='moderator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderated_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='moderatedtext',
            name='original',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderated_tasks', to='mine.Text'),
        ),
    ]
