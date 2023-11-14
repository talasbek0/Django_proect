from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from .models import *
from django.http import HttpResponse


def body(request):
    return render(request, 'body.html')


def index(request):
    value = Pizza.objects.all()
    value2 = Menu.objects.all()

    context = {
        'value': value,
        'value2': value2
    }
    return render(request, 'about.html', context)


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    reviews = Review.objects.all()

    return render(request, 'users.html', {'form': form, 'reviews': reviews})


def menu(request):
    value2 = Menu.objects.all()
    context = {
        'value': value2
    }
    return render(request, 'about.html', context)


def regis(request):
    if request.method == 'POST':
        pizza_name = request.POST.get('pizza_name')
        quantity = request.POST.get('quantity')
        delivery_address = request.POST.get('delivery_address')  # аналогично для delivery_address
        phone_number = request.POST.get('phone_number')

        PizzaOrder.objects.create(
            pizza_name=pizza_name,
            quantity=quantity,
            delivery_address=delivery_address,
            phone_number=phone_number
        )

        return HttpResponse('Ваш заказ скоро будет доставлен, будьте в связи!')
    return render(request, 'delivery.html')