from django.db import models


class Pizza(models.Model):
    title = models.TextField(max_length=20, verbose_name='Название пиццы')
    description = models.TextField(max_length=100, verbose_name='Описание пиццы')
    img = models.ImageField(upload_to='img/%Y/%m/%d', blank=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Раздел')
    list_value = models.TextField(max_length=150, verbose_name='Список продуктов')
    # pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='menu_items', verbose_name='Пицца')

    def __str__(self):
        return self.title


class PizzaOrder(models.Model):
    pizza_name = models.CharField(max_length=100, verbose_name='Название пиццы')
    quantity = models.IntegerField(verbose_name='Количество')
    delivery_address = models.TextField(verbose_name='Адрес')
    phone_number = models.CharField(max_length=12, verbose_name='Номер клиента')

    def __str__(self):
        return f"{self.quantity} шт. {self.pizza_name} для доставки по адресу: {self.delivery_address}"


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    text = models.TextField(verbose_name='Отзыв')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.name} - {self.rating}'