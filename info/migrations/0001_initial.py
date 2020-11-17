# Generated by Django 3.1.2 on 2020-11-17 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aggregateList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('jamb', models.PositiveIntegerField()),
                ('post_utme', models.PositiveIntegerField()),
                ('aggregate', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Aggregate Table',
            },
        ),
        migrations.CreateModel(
            name='infoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=80)),
                ('info', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Information',
            },
        ),
    ]
