# Generated by Django 3.1.5 on 2021-02-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=140)),
                ('correct_answer', models.CharField(max_length=1)),
                ('solution', models.CharField(max_length=210)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('email_id', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=10)),
                ('contact_no', models.IntegerField()),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
