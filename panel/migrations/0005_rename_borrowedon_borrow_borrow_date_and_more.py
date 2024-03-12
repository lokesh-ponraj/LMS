# Generated by Django 5.0.2 on 2024-03-10 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_remove_borrow_borrow_date_remove_borrow_due_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='borrowedOn',
            new_name='borrow_date',
        ),
        migrations.RenameField(
            model_name='borrow',
            old_name='dueDate',
            new_name='due_date',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='fineAmount',
        ),
        migrations.AddField(
            model_name='borrow',
            name='fine',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.book'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.student'),
        ),
    ]
