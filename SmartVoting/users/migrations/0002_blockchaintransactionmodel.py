# Generated by Django 4.0.5 on 2022-11-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockChainTransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_index', models.CharField(max_length=100)),
                ('c_timestamp', models.CharField(max_length=100)),
                ('c_sender', models.CharField(max_length=100)),
                ('c_recipient', models.CharField(max_length=100)),
                ('c_vote', models.CharField(max_length=100)),
                ('c_proof', models.CharField(max_length=100)),
                ('c_previous_hash', models.CharField(max_length=100)),
                ('p_index', models.CharField(max_length=100)),
                ('p_timestamp', models.CharField(max_length=100)),
                ('p_sender', models.CharField(max_length=100)),
                ('p_recipient', models.CharField(max_length=100)),
                ('p_vote', models.CharField(max_length=100)),
                ('p_proof', models.CharField(max_length=100)),
                ('p_previous_hash', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'BlockChainTransactiontable',
            },
        ),
    ]
