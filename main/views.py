from django.shortcuts import render

#LoginViewクラスを使う
from django.contrib.auth.views import LoginView

#汎用ビューをインポート
from django.views import View

#メッセージを表示するライブラリーをインポート
from django.contrib import messages

# Create your views here.

#ドキュメントルートの処理
def index(request):
    context = {}
    return render(request,'main/index.html',context)

#extendsやblock〇〇の練習用の処理
def extends_block_test(request):
    context = {}
    return render(request,'main/extends_block_test.html',context)

#LoginViewクラスを継承してクラスLoginでログイン処理する
#汎用ビューを継承(左に)
class Login(LoginView,View):
    #ログイン画面の指定
    template_name = 'main/login.html'
    
    #汎用ビューをを使ってオリジナルの関数を定義
    #GET状態なら
    def get(self,request):
        context = {
            #'grecaptcha_sitekey': os.environ['GRECAPTCHA_SITEKEY'],
        }
        #POST状態
        if request.method == 'POST':
            #-----reCAPTCHA検証----------
            #recaptcha_token = request.POST.get("g-recaptcha-response")
            #res = grecaptch_request(recaptcha_token)
            #if not res:
                #messages.error(request,'reCAPTCHA FAIL')
                #return render(request,'main/login19981010.html',context)
            #-----reCAPTCHA検証----------
            pass
        return render(request,'main/login.html',context)
    
    def form_valid(self,form):
        #messages.success(self.request,'ログイン完了です!')
        return super().form_valid(form)


def task_main(request):
    mes = 'ログイン中'
    context = {
        'dosukoi' : 'どすこい',
        'message' : mes,
    }
    return render(request,'main/task_main.html',context)