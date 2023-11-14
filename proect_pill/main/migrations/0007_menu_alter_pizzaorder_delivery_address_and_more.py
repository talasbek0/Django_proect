# Generated by Django 4.2.7 on 2023-11-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_pizza_type_pizzaorder_pizza_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Раздел')),
                ('description', models.TextField(max_length=100, verbose_name='меню')),
            ],
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='delivery_address',
            field=models.TextField(verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='Номер клиента'),
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='pizza_name',
            field=models.CharField(max_length=100, verbose_name='Название пиццы'),
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
    ]
