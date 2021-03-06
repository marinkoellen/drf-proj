# Generated by Django 3.0.8 on 2020-08-23 06:09

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_delete_pledge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='campaign_end_date',
            field=models.DateTimeField(default=projects.models.get_closing_date),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
