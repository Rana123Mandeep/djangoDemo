# Generated by Django 4.0.6 on 2024-08-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]