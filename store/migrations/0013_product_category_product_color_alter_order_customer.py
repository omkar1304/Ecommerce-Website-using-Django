# Generated by Django 4.0.4 on 2022-05-10 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('T', 'Tablet'), ('L', 'Laptop'), ('D', 'Desktop'), ('F', 'Fashion'), ('G', 'Gadgets'), ('A', 'Appliances'), ('H', 'None')], default='N', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
    ]