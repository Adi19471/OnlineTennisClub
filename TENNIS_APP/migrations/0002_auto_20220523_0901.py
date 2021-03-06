# Generated by Django 3.0 on 2022-05-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TENNIS_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('day', models.CharField(max_length=250)),
                ('time', models.TimeField()),
                ('duration_of_game', models.CharField(max_length=40)),
                ('number_of_player', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=4, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
    ]
