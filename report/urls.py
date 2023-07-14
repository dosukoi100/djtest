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
    
    ###Cashbookモデルのtotalフィールドの総計を取得する
    
    #オリジナル
    path('cashbook_year/',views.cashbook_year),
    #sum関数
    path('cashbook_year_def_sum/',views.cashbook_year_def_sum),
    #生SQL文からの取得
    path('cashbook_year_sql_sum/',views.cashbook_year_sql_sum),
    #-----models.forms.admin.urls.views.htmlの統合練習用----
]