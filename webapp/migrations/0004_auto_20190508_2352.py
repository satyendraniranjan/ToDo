# Generated by Django 2.0.13 on 2019-05-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_todo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(default='todo', max_length=255),
        ),
    ]
