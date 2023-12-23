from datetime import timezone
from django.db import models

class Coins(models.Model):
    title = models.CharField(max_length=20)
    old_price = models.IntegerField(default=10)
    price = models.IntegerField(default=10)
    time = models.DateTimeField(auto_now=True )
    
class Wallet(models.Model):
    money = models.IntegerField(default=1000)
    coins = models.IntegerField(default=1)