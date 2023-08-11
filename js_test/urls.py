from django.urls import path,include
from js_test import views

urlpatterns = [
    path('length/',views.length),#inputタグのnumber属性の入力数制限
    path('callback/',views.callback),#callback関数
    path('unsync/',views.unsync),#非同期通信
    path('prep1/',views.prep1),#予習用
    path('prep2/',views.prep2),#予習用
    path('prep3',views.prep3),#予習用
    path('test1/',views.test1),#当日教材用
    path('test2/',views.test2),#当日教材用
    path('test3/',views.test3),#当日教材用
    path('test4/',views.test4),#当日教材用
]