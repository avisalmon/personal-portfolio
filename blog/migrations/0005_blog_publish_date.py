# Generated by Django 3.0.5 on 2020-04-29 04:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200429_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
