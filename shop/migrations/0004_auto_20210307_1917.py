# Generated by Django 3.1.7 on 2021-03-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Phone',
            field=models.IntegerField(default=''),
        ),
    ]
