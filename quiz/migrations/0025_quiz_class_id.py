# Generated by Django 5.1.3 on 2024-11-06 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allClass', '0003_remove_myclass_quizzes'),
        ('quiz', '0024_quiz_active_quiz_instructor_fullstudentanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allClass.myclass'),
        ),
    ]
