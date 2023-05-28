#入力フォームformsをインポート
from pyexpat import model
from django import forms
#get_user_modelをインポート
from django.contrib.auth import get_user_model
#エラーを出力するライブラリー
#from django.core.exceptions import ValidationError

#forms.ModelFormを継承
class UserCreationForm(forms.ModelForm):
    password = forms.CharField()
    #new
    #confirmpasswd = forms.CharField()
 
    class Meta:
        #emailで登録 new username追加
        model = get_user_model()
        fields = ('email','username',)
    #パスワードを整形(暗号化)して格納する関数
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password
    '''
    #確認用パスワードを整形(暗号化)して格納する関数new
    def clean_comfirmpasswd(self):
        confirmpasswd = self.cleaned_data.get("confirmpasswd")
        return confirmpasswd
    '''
    
    #ユーザーを登録する関数
    def save(self, commit=True):
        user = super().save(commit=False)
        #ここでパスワードを復号
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user