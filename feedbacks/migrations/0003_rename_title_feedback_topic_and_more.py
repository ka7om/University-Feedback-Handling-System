# Generated by Django 5.1.3 on 2024-11-29 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_rename_student_feedback_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='title',
            new_name='topic',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='User',
            new_name='user',
        ),
    ]
