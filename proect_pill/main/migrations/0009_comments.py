# Generated by Django 4.2.7 on 2023-11-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_menu_description_menu_pizza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=100, verbose_name='Комментарии')),
                ('created', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
