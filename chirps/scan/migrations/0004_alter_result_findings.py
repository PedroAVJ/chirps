# Generated by Django 4.2.2 on 2023-06-29 16:29

from django.db import migrations
import fernet_fields.fields


class Migration(migrations.Migration):
    dependencies = [
        ("scan", "0003_result_findings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="findings",
            field=fernet_fields.fields.EncryptedTextField(default="[]"),
        ),
    ]
