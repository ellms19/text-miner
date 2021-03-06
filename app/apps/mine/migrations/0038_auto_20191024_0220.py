# Generated by Django 2.0 on 2019-10-23 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0037_auto_20191016_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='task',
        ),
        migrations.AddField(
            model_name='notification',
            name='link',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
