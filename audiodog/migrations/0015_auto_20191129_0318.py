# Generated by Django 2.2.7 on 2019-11-29 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiodog', '0014_auto_20191129_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='ciudad',
            field=models.TextField(max_length=100),
        ),
    ]
