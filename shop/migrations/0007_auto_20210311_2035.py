# Generated by Django 3.1.7 on 2021-03-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210311_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Order_Id',
            new_name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='Order_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
