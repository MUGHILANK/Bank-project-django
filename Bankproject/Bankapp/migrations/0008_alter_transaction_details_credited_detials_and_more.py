# Generated by Django 5.1.4 on 2025-01-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0007_remove_transaction_details_my_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_details',
            name='credited_detials',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='transaction_details',
            name='deposit_detials',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
