# Generated by Django 3.0.8 on 2020-08-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='display_picture',
            field=models.URLField(default='https://via.placeholder.com/300.jpg'),
            preserve_default=False,
        ),
    ]
