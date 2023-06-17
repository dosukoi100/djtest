#報告関係reportのフォームを定義

from django import forms
from report.models import Cost,Incomes

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