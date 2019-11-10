# Generated by Django 2.0 on 2019-10-10 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0028_remove_classroom_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedtask',
            name='task',
        ),
        migrations.RemoveField(
            model_name='completedtask',
            name='user',
        ),
        migrations.AddField(
            model_name='miner',
            name='task',
            field=models.ManyToManyField(through='mine.Text', to='mine.Task'),
        ),
        migrations.AlterField(
            model_name='text',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mine.Miner'),
        ),
        migrations.DeleteModel(
            name='CompletedTask',
        ),
    ]