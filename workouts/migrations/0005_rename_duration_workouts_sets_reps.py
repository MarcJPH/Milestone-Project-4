# Generated by Django 3.2.8 on 2021-11-25 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_auto_20211124_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workouts',
            old_name='duration',
            new_name='sets_reps',
        ),
    ]
