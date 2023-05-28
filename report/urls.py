from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('cost/',views.cost),
    path('income/',views.income),
]