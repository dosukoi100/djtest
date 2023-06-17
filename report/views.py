from django.shortcuts import render

from django.contrib.auth import get_user,get_user_model

from main.models.profile_models import Profile

from report.forms import CostForm,IncomesForm

# Create your views here.

#報告のインデックス関数
def index(request):
    context = {}
    return render(request,'report/index.html',context)

#-------支出の関数--------------------------

#################################################
#今回はセッションや関数で計算式を実行しない場合の方法です#
#セッションを張らないので一回で確定してしまいますが簡単に#
#モデルにオブジェクト(レコード)を格納するのと、モデルの自#
#由な取り出しを目的にしています。#####################
#################################################

#経費(cost)の入力
def cost(request):
    #GET時
    
    #----ログイン中のユーザー情報を取得----
    user = get_user(request)
    user_id = user.id
    
    #---Profileモデルからログイン中のmember_numberを取得---
    
    #get(pk=user_id)でも良いが、Profileモデルのフィールドu
    #sername_idで指定(こちらが正式)
    member_number = Profile.objects.get(username_id=user_id)
    profile_member_number = member_number.member_number
    
    '''
    #-------検証:モデルの取得について------
    all_model = Profile.objects.all()
    #ログイン中のprofileモデルのオブジェクト(レコード)が帰ってくる
    print(type(member_number))
    #QuerySetで帰ってくる
    print(type(all_model))
    
    #Profileモデルのオブジェクトは関数__str__()で文字列が帰ってくる
    for i in all_model:
        print(i)
    
    #Profileモデルの値はQuerySetで帰ってくる
    for i in all_model.values():
        print(i)
    '''
    
    form = CostForm(request.POST.copy())
    context = {
        'cost_form' : form,#動的ファイルを使う時に使用
        'user_id' : user_id,
        'profile_member_number' : profile_member_number,
        #'profile_type' : print(type(member_number)),#profile_type,
        }
    #POST時
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        form = CostForm(dic)
    
    if form.is_valid():
        form.save()
    
    return render(request,'report/cost.html',context)

#経費の確認・修正
def cost_conform(request):
    context = {}
    return render(request,'report/cost_conform.html',context)

#-------支出の関数--------------------------

#収入の関数
def incomes(request):
    #GET
    user = get_user(request)
    user_id = user.id
    
    member_number = Profile.objects.get(username_id = user_id)
    profile_member_number = member_number.member_number
    
    form = IncomesForm(request.POST.copy())
    context = {
        'incomes_form' : form,
        'user_id' : user_id,
        'profile_member_number' : profile_member_number,
    }
    
    #POST
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        form = IncomesForm(dic)
        
    if form.is_valid():
        form.save()
    
    return render(request,'report/incomes.html',context)
