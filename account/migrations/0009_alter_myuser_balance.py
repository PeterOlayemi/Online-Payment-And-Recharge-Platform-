# Generated by Django 4.1.4 on 2023-03-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_myuser_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
    ]
