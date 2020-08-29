# Generated by Django 3.0.8 on 2020-08-29 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20200826_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='campaign_end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='dream_goal',
        ),
        migrations.AddField(
            model_name='project',
            name='project_duration',
            field=models.IntegerField(default=21),
            preserve_default=False,
        ),
    ]