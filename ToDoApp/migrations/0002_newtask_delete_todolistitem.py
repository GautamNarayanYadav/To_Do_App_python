# Generated by Django 4.0.2 on 2022-03-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AddTask', models.CharField(max_length=30)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='TodoListItem',
        ),
    ]
