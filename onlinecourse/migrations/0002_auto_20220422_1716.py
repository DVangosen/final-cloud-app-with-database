# Generated by Django 3.1.3 on 2022-04-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='content',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='title',
        ),
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='question',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
