# Generated by Django 3.0.8 on 2020-08-26 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_project_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_categories', to='projects.Category'),
        ),
    ]