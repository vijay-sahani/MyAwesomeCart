# Generated by Django 3.1.7 on 2021-03-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_order_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_id', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Order_update', models.CharField(default='', max_length=500)),
                ('Cart_item', models.CharField(default='', max_length=500)),
                ('Email', models.CharField(default='', max_length=100)),
            ],
        ),
    ]