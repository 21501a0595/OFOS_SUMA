# Generated by Django 5.1.3 on 2024-11-06 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_cartitem_ordered'),
        ('restaurant', '0003_alter_restaurant_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant'),
            preserve_default=False,
        ),
    ]