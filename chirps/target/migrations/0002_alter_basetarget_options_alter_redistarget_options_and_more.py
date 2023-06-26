# Generated by Django 4.2.2 on 2023-06-21 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('target', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basetarget',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='redistarget',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AddField(
            model_name='basetarget',
            name='polymorphic_ctype',
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='polymorphic_%(app_label)s.%(class)s_set+',
                to='contenttypes.contenttype',
            ),
        ),
    ]
