# Generated by Django 4.1.1 on 2022-11-30 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_blockchaintransactionmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlockChainTransactionModel',
        ),
    ]
