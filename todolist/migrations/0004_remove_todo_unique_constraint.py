# Generated by Django 5.1.5 on 2025-02-02 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todo_unique_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='todo',
            name='unique_constraint',
        ),
    ]
