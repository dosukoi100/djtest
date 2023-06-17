from django.urls import path,include
from report import views

urlpatterns = [
    path('',views.index),#タスク選択画面
    path('cost/',views.cost),#cost入力画面
    path('cost_conform/',views.cost_conform),#costの確認、修正画面
    path('incomes/',views.incomes), 
]