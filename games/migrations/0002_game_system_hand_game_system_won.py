# Generated by Django 4.0.4 on 2022-04-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='system_hand',
            field=models.CharField(choices=[('ROCK', 'rock'), ('PAPER', 'paper'), ('SCISSORS', 'scissors')], default='PAPER', max_length=8),
        ),
        migrations.AddField(
            model_name='game',
            name='system_won',
            field=models.BooleanField(default=False),
        ),
    ]
