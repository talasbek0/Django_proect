from main.views import index, regis, body, reviews
from django.urls import path

urlpatterns = [
    path('', body),
    path('menu/', index, name='menu'),
    path('zakaz/', regis, name='zakaz'),
    path('body/send_text/', reviews, name='reviews'),
]