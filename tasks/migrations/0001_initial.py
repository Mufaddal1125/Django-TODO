# Generated by Django 3.0.8 on 2020-08-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskData',
            fields=[
                ('priority', models.IntegerField(primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=64)),
            ],
        ),
    ]
