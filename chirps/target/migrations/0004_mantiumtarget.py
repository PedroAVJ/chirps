# Generated by Django 4.2.2 on 2023-06-22 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('target', '0003_alter_redistarget_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='MantiumTarget',
            fields=[
                (
                    'basetarget_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='target.basetarget',
                    ),
                ),
                ('app_id', models.CharField(max_length=256)),
                ('token', models.CharField(max_length=2048)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('target.basetarget',),
        ),
    ]
