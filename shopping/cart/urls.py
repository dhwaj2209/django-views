from django.urls import path
from . import views

urlpatterns = [
    path('function', views.index, name='index'),
    #path('', views.date_view),
    path('class', views.cart_list.as_view(), name='list'),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('create/', views.item_create, name='create'),
    path('center/', views.center_view, name='center'),
] 