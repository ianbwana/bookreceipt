# Generated by Django 3.2 on 2021-04-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210413_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
