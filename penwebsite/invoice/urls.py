from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('order_page',views.orderPage,name='order_page'),
    path('payments',views.payments,name='payments'),
    path('order_page2',views.order_page2,name='order_page2')
]