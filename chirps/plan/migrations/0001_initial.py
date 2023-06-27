# Generated by Django 4.2.2 on 2023-06-24 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('is_template', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=256)),
                ('query_string', models.TextField()),
                ('query_embedding', models.TextField()),
                ('regex_test', models.TextField()),
                ('severity', models.IntegerField()),
                (
                    'plan',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.plan'),
                ),
            ],
        ),
    ]