# Generated by Django 3.1.2 on 2020-11-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregate', '0003_auto_20201117_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aggregatelist',
            name='aggregate',
            field=models.CharField(max_length=50),
        ),
    ]
