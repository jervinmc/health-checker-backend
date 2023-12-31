# Generated by Django 4.0 on 2023-08-17 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('endpoint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='endpoint',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='endpoint'),
        ),
    ]
