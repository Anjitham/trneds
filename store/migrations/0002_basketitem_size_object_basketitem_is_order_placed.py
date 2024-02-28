# Generated by Django 5.0.2 on 2024-02-28 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='Size_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.size'),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='is_order_placed',
            field=models.BooleanField(default=False),
        ),
    ]
