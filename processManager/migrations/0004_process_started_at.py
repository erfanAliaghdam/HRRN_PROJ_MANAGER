# Generated by Django 4.1 on 2022-08-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processManager', '0003_process_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='started_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
