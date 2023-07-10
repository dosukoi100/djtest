from django.urls import path,include
from report import views

urlpatterns = [
    path('',views.index),#タスク選択画面
    path('cost/',views.cost),#cost入力画面
    path('cost_conform/',views.cost_conform),#costの確認、修正画面
    path('cost_thankyou/',views.cost_thankyou),#costの完了画面
    path('incomes/',views.incomes), 
    #-----models.forms.admin.urls.views.htmlの統合練習用----
    path('test1/',views.test1),
    
    path('sort/',views.sort),#sort入力
    path('sort_conform/',views.sort_conform),#sortの確認・訂正
    path('sort_thankyou/',views.sort_thankyou), 
    
    path('cashbook/',views.cashbook),
    path('cashbook/conform/',views.cashbook_conform),
    path('cashbook/thankyou/',views.cashbook_thankyou),
    
    #-----models.forms.admin.urls.views.htmlの統合練習用----
]