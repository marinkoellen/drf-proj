# Generated by Django 3.0.8 on 2020-08-29 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20200829_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='dream_goal',
            field=models.IntegerField(default=5000),
            preserve_default=False,
        ),
    ]