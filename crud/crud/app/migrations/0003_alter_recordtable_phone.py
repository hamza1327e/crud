# Generated by Django 5.0.6 on 2024-05-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_recordtable_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordtable',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]