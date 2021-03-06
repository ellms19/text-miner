# Generated by Django 2.0 on 2019-05-12 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeratedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('moderator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('raw_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mine.Text')),
            ],
        ),
    ]
