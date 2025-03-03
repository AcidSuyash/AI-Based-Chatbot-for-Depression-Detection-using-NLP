# Generated by Django 3.2.7 on 2022-03-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_chatbotuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='negCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userscore',
            name='posCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='score',
            field=models.FloatField(default=0.0),
        ),
    ]
