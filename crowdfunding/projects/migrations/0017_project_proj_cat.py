# Generated by Django 3.0.8 on 2020-08-25 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proj_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='projects.Category'),
        ),
    ]
