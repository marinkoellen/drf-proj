# Generated by Django 3.0.8 on 2020-08-29 04:16

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20200829_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_duration',
        ),
        migrations.AddField(
            model_name='project',
            name='campaign_end_date',
            field=models.DateTimeField(default=projects.models.get_closing_date),
        ),
    ]