# Generated by Django 3.1 on 2020-09-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testid', models.IntegerField(verbose_name='房间号')),
                ('count', models.IntegerField(verbose_name='人数')),
            ],
        ),
        migrations.CreateModel(
            name='UAV',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('a1', models.FloatField(max_length=20, verbose_name='a1')),
                ('a2', models.FloatField(max_length=20, verbose_name='a2')),
            ],
        ),
    ]
