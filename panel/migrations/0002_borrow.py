# Generated by Django 5.0.2 on 2024-03-10 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=100, unique=True)),
                ('borrow_date', models.DateField()),
                ('due_date', models.DateField()),
                ('fine', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.student')),
            ],
        ),
    ]
