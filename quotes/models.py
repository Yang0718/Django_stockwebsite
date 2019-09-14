from django.db import models

# models就是django的DB
# 在建完DB之後，永遠記得要先migrate，並推上去。即以下兩個指令
# python manage.py makemigrations
# python manage.py migrate
class StockDB(models.Model):
    ticker = models.CharField(max_length=10) # 因為存的是股票名字，也就是文字，所以用CharField

    def __str__(self):
        return self.ticker

# 創好models後，接著為了讓admin頁面能管理這個model，去admin.py寫