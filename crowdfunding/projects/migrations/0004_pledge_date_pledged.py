# Generated by Django 3.0.8 on 2020-08-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200823_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='date_pledged',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
