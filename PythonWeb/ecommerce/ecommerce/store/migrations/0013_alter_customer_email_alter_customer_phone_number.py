# Generated by Django 4.0.3 on 2022-04-03 16:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_customer_email_alter_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=120),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=22, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number.', regex='^[0-9+\\s]+$')]),
        ),
    ]
