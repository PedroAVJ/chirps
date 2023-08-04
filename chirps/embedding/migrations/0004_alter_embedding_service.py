# Generated by Django 4.2.3 on 2023-08-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('embedding', '0003_alter_embedding_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embedding',
            name='service',
            field=models.CharField(
                choices=[
                    ('cohere', 'cohere'),
                    ('localhost', 'Locally Hosted: NOT IMPLEMENTED'),
                    ('OpenAI', 'OpenAI'),
                ],
                max_length=256,
            ),
        ),
    ]