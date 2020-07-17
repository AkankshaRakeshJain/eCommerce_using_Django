from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('category/<str:pk>',views.category,name='category'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('address/',views.address,name='address'),

]
