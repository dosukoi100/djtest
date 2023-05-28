from django.shortcuts import render

# Create your views here.

#報告のインデックス関数
def index(request):
    context = {}
    return render(request,'report/index.html',context)

#支出の関数
def cost(request):
    context = {}
    return render(request,'report/cost.html',context)

#収入の関数
def income(request):
    context = {}
    return render(request,'report/income.html',context)
