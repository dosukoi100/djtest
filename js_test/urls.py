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
    path('basic1/',views.basic1),#勉強会後ともスタに沿った物
    path('basic2/',views.basic2),#勉強会後ともスタに沿った物
    path('basic3/',views.basic3),#勉強会後ともスタに沿った物
    path('basic3-1/',views.basic3_1),#勉強会後ともスタに沿った物
    path('basic3-2/',views.basic3_2),#Ajax通信のところ
    path('jq1/',views.jq1),#jQueryの学習
    path('vue1/',views.vue1),#Vue.jsの学習
    path('vue2/',views.vue2),#Vue.jsの学習 写真・コメント等
    path('slide1/',views.slide1),#スライドショーを表示
    path('slide2/',views.slide2),#Ajax通信・jQuery・Vue.jsを使ったスライドショー
    path('ani1/',views.ani1),#アニメーションの学習Web Animations API
    path('ani2/',views.ani2),#ともすたWeb Animations API
    path('ani3/',views.ani3),#ぷよぷよアニメーション
]