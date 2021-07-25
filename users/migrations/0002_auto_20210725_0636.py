# Generated by Django 3.2.5 on 2021-07-25 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='country',
            field=models.CharField(default='null', max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='phone',
            field=models.CharField(default='null', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='state',
            field=models.CharField(default='null', max_length=48, null=True),
        ),
    ]
