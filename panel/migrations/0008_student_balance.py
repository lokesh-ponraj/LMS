# Generated by Django 5.0.2 on 2024-03-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
