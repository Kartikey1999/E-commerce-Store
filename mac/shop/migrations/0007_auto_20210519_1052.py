# Generated by Django 2.2.12 on 2021-05-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderupdate',
            old_name='time_stamp',
            new_name='timestamp',
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default=''),
        ),
    ]