# Generated by Django 4.0.3 on 2022-04-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_customer_email_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=120, unique=True),
        ),
    ]