# Generated by Django 3.2.19 on 2023-06-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0002_remove_yogaexercise_yoga_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yogaday',
            name='yoga_exercise',
        ),
        migrations.AddField(
            model_name='yogaday',
            name='yoga_exercises',
            field=models.ManyToManyField(to='yoga.YogaExercise'),
        ),
    ]
