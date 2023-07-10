#報告関係reportのフォームを定義

from django import forms
from report.models import Cost,Incomes,test1,Debit,Credit,Sort,Cashbook

#経費フォームの定義
class CostForm(forms.ModelForm):
    class Meta:
        #モデルの指定
        model = Cost
        #入力項目の指定
        fields = {
            'username',
            'member_number',
            'seireki',
            'koutuuhi',
            'shokuhi',
            'youfukuhi',
            'zeikinn',
            'hoken',
            'kounetuhi',
            'yachin',
            'chuushajoudai',
            'zapi',
            'total',
        }
        

#収入フォームの定義
class IncomesForm(forms.ModelForm):
    class Meta:
        model = Incomes
        
        fields = {
            'username',
            'member_number',
            'seireki',
            'salary',
            'bonus',
            'temporary_income',
            'total',
        }
        

#-----models.forms.admin.urls.views.htmlの統合練習用----
#歩数を記録するtest1

class test1Form(forms.ModelForm):
    class Meta:
        model = test1
        fields = {
            'username',
            'member_number',
            'walks',
            'insert_day',
        }

#借方(Debit)
class DebitForm(forms.ModelForm):
    class Meta:
        model = Debit
        fields = {
            'debit_item',
        }
        
#借方(Credit)
class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = {
            'credit_item',
        }
        
#仕分(Sort)
class SortForm(forms.ModelForm):
    class Meta:
        model = Sort
        fields = {
            'exec_user',
            'exec_user_number',
            'exec_day',
            'debit',
            'debit_amount',
            'credit',
            'credit_amount',
            'comment',
        }
        
#Cost,Incomesからのtotalを格納するCashbook
class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = {
            'exec_user',
            'exec_user_number',
            'username',
            'member_number',
            'seireki',
            'income_total',
            'cost_total',
            'total',
        }
        

#-----models.forms.admin.urls.views.htmlの統合練習用----