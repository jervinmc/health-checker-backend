# Generated by Django 4.0 on 2023-08-17 06:16

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('endpoint', models.CharField(blank=True, max_length=255, null=True, verbose_name='package_name')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='status')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
