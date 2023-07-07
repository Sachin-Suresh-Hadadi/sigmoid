from app import views
from django.urls import path

urlpatterns=[
   path('',views.index, name=''),
   path('conferm',views.conferm, name='conferm'),
   path('orderlist',views.orderlist, name='orderlist')
]