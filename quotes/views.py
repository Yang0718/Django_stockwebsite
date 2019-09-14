from django.shortcuts import render, redirect
from .models import StockDB
from .forms import StockForm # 自己建file
from django.contrib import messages

# Create your views here.
def home(request):
    # pk_6a5adede513a4469a9044fdc3ed4bc23
    # 開始用API囉
    import requests
    import json

    if request.method=='POST':
        ticker = request.POST['ticker_symbol'] # ['ticker_symbol']裡的ticker代表的就是寫在搜尋框框裡面的字，e.g. goog
        # 接著把ticker塞進網址中
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/quote?token=pk_6a5adede513a4469a9044fdc3ed4bc23")
    
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'error...'

        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol above..."}) # 此處的'ticker'是指上面做得的變數ticker，不是在base.html中input的name

def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json

    if request.method=='POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been Added successfully"))
            return redirect('add_stock') # redirect:重新導向其他頁面

    else:
        ticker = StockDB.objects.all() # 把建好的StockDB裡面全部的東西都叫出來
        output=[]
        for ticker_item in ticker: # 把ticker裡面的所有股票一個個叫出來
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ str(ticker_item) +"/quote?token=pk_6a5adede513a4469a9044fdc3ed4bc23")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = 'error...'
        return render(request, 'add_stock.html', {'ticker' : ticker, 'output' : output})

def delete(request, stock_id):
    item = StockDB.objects.get(pk=stock_id) # pk:primary key
    item.delete() # 一行就能把資料從Db刪掉了
    messages.success(request, ("Stock has been deleted"))
    return redirect(delete_stock)


def delete_stock(request):
    ticker = StockDB.objects.all()

    return render(request, 'delete_stock.html', {'ticker':ticker})