# Generated by Django 4.0.3 on 2022-04-06 14:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_shippingaddress_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
    ]
