# Generated by Django 4.2.2 on 2023-06-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('target', '0004_mantiumtarget'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantiumtarget',
            name='top_k',
            field=models.IntegerField(default=100),
        ),
    ]
