# Generated by Django 4.0.3 on 2022-04-06 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]