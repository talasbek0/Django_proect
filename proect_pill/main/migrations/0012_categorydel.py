# Generated by Django 4.2.7 on 2023-11-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_review_delete_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Доб.Категории')),
            ],
        ),
    ]