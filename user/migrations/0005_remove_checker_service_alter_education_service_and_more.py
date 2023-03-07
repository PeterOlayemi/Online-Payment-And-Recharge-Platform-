# Generated by Django 4.1.4 on 2023-03-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_eduservice_checker_service_alter_education_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checker',
            name='service',
        ),
        migrations.AlterField(
            model_name='education',
            name='service',
            field=models.IntegerField(choices=[(1, 'WAEC RESULT CHECKER = #5000'), (2, 'NECO RESULT CHECKER = #2000')], default=0),
        ),
        migrations.DeleteModel(
            name='EduService',
        ),
    ]
