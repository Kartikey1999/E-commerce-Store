# Generated by Django 2.2.12 on 2021-05-18 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210517_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=11)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]
