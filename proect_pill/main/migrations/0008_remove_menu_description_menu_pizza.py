# Generated by Django 4.2.7 on 2023-11-12 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_menu_alter_pizzaorder_delivery_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
        migrations.AddField(
            model_name='menu',
            name='pizza',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='main.pizza', verbose_name='Пицца'),
            preserve_default=False,
        ),
    ]
