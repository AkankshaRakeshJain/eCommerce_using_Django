# Generated by Django 3.0.7 on 2020-07-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_auto_20200710_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
