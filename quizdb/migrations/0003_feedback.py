# Generated by Django 3.1.5 on 2021-02-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizdb', '0002_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
    ]
