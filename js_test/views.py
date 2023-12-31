from django.shortcuts import render,redirect

#メッセージを表示するライブラリーをインポート
from django.contrib import messages

#リクエストやURLの検証をするurllibをインポートしてrequestとparseをインポート
from urllib import request,parse

#sslとjsonをインポート
import json,ssl

#環境変数からyamlファイルを呼び出せるようにosをインポート
import os

import datetime

# Create your views here.

#inputタグのnumber属性の場合の入力数の制限
def length(request):
    context = {}
    return render(request,'js_test/length.html',context)

#reCAPTCHAのトークンを検証する関数
def grecaptch_request(token):
    #sslのバージョンを指定
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    #reCAPTCHAapiのURLを記述
    url = "https://www.google.com/recaptcha/api/siteverify"
    #リクエストを送るヘッダーを用意する。{}内は丸写し 
    headers = {'content-type' : 'application/x-www-form-urlencoded'} 
    #シークレットキーとトークンを格納 
    #公式ドキュメントからの流用。キーは丸写し 
    data = { 
    'secret' : os.environ['GRECAPTCHA_SECRETKEY'], 
    'response' : token, 
    } 
    #dataを検証して再度dataとする 
    data = parse.urlencode(data).encode() 
    #urllibのrequestを使って各値をリクエストをします 
    req = request.Request( 
    url, 
    method="POST", 
    headers=headers, 
    data=data, 
    ) 
    #reqをcontext(ssl)で開く 
    f = request.urlopen(req,context=context) 
    #jsonでfで開いて格納 
    response = json.loads(f.read()) 
    #f閉じる 
    f.close() 
    #戻ってきたresponseの中にキーで'success'があるのでそれを返す 
    #TrueかFalseが帰ってくる 
    return response['success']

#callback関数
def callback(request):
    context = {
            'grecaptcha_sitekey': os.environ['GRECAPTCHA_SITEKEY'],
    }
    if request.method == 'POST':
        #-----reCAPTCHA検証----------
        recaptcha_token = request.POST.get("g-recaptcha-response")
        res = grecaptch_request(recaptcha_token)
        if not res:
            messages.error(request,'reCAPTCHA FAIL')
            return render(request,'js_test/callback.html',context)
            #-----reCAPTCHA検証----------
    return render(request,'js_test/callback.html',context)

#非同期通信
def unsync(request):
    context = {}
    return render(request,'js_test/unsync.html',context)

#予習用1
def prep1(request):
    now_time = datetime.datetime.now()
    context = {
        'now_time' : now_time,
    }
    return render(request,'js_test/prep1.html',context)

#予習用2
def prep2(request):
    context = {}
    return render(request,'js_test/prep2.html',context)

#予習用
def prep3(request):
    context = {}
    return render(request,'js_test/prep3.html',context)

#勉強会用
def test1(request):
    context = {}
    return render(request,'js_test/test1.html',context)

#勉強会用
def test2(request):
    context = {}
    return render(request,'js_test/test2.html',context)

#勉強会用
def test3(request):
    context = {}
    return render(request,'js_test/test3.html',context)

#勉強会用
def test4(request):
    context = {}
    return render(request,'js_test/test4.html',context)

#勉強会後の学び直し
def basic1(request):
    context = {
        'now_time' : datetime.datetime.now(),
        'year' : datetime.datetime.now().year,
        'month' : datetime.datetime.now().month,
        'day' : datetime.datetime.now().day,
    }
    return render(request,'js_test/basic1.html',context)

 #勉強会後の学び直し
def basic2(request):
    context = {}
    return render(request,'js_test/basic2.html',context)

#勉強会後の学び直し
def basic3(request):
    context = {}
    return render(request,'js_test/basic3.html',context)

#Djangoでの画面の表示
def basic3_1(request):
    #テンプレートタグfor用
    lists = [1,2,3,4]
    context = {
        "lists" : lists,
    }
    return render(request,'js_test/basic3-1_django-for.html',context)

#Ajax通信
def basic3_2(request):
    context = {}
    return render(request,'js_test/basic3-2_ajax.html',context)

#jQueryの学習
def jq1(request):
    context = {}
    return render(request,'js_test/jq1.html',context)

#Vue.jsの学習
def vue1(request):
    context = {
        'message' : 'どすこいDjango',
    }
    return render(request,'js_test/vue1.html',context)

#Vue.jsの学習 写真・コメント・作成者を表示する
def vue2(request):
    context = {}
    return render(request,'js_test/vue2.html',context)

#スライドショーを表示
def slide1(request):
    context = {}
    return render(request,'js_test/slide1.html',context)

#Ajax通信・jQuery・Vue.jsを使ったスライドショー
def slide2(request):
    context = {}
    return render(request,'js_test/slide2.html',context)

#アニメーションの学習Web Animations API
def ani1(request):
    context = {}
    return render(request,'js_test/ani1.html',context)

#ともすたWeb Animations API
def ani2(request):
    context = {}
    return render(request,'js_test/ani2.html',context)

#ぷよぷよアニメーション
def ani3(request):
    context = {}
    return render(request,'js_test/ani3.html',context)


