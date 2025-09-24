from django.urls import path
from . import views

urlpatterns = [
    path('function', views.index, name='index'),
    #path('', views.date_view),
    path('class', views.cart_list.as_view())
]