# Generated by Django 5.1.3 on 2024-11-06 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allClass', '0002_myclass_code_classrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myclass',
            name='quizzes',
        ),
    ]