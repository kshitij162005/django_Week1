# Generated by Django 5.1.7 on 2025-04-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='details',
            field=models.CharField(default='No details provided', max_length=500),
        ),
        migrations.AddField(
            model_name='feature',
            name='name',
            field=models.CharField(default='Unnamed Feature', max_length=100),
        ),
    ]
