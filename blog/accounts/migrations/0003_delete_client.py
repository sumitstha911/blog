# Generated by Django 4.1.7 on 2023-02-22 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_client_birth_date_alter_client_company_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
    ]
