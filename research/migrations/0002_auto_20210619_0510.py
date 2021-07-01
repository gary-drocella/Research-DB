# Generated by Django 3.2.4 on 2021-06-19 05:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
        migrations.AddField(
            model_name='note',
            name='note_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paper',
            name='notes',
            field=models.ManyToManyField(blank=True, to='research.Note'),
        ),
        migrations.AddField(
            model_name='paper',
            name='title',
            field=models.CharField(default='The Design and Implementation of a Log-Structured File System', max_length=128, validators=[django.core.validators.RegexValidator(code='title', message='Paper title can only contain alphanumeric and space characters.', regex='^([0-9a-zA-Z]+\\s{0,1})*$')]),
        ),
    ]