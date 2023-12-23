from urllib import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from .models import Coins, Wallet
from .forms import AuthorizationForm

def App(request):
    context = {
        'coins': Coins.objects.all(),
        'items': Wallet.objects.all()
    }
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'app/home.html', context)

def buy(request):
    pricee = Coins.objects.get(id = 1)
    moneyy = Wallet.objects.get(id = 1)
    
    if moneyy.money >= pricee.price:
        moneyy.coins += 1
        moneyy.money = moneyy.money - pricee.price
        moneyy.save()
        return redirect('main')
    else:
        return redirect('main')
    
def sell(request):
    pricee = Coins.objects.get(id = 1)
    moneyy = Wallet.objects.get(id = 1)
    
    if moneyy.coins > 0:
        moneyy.coins = moneyy.coins - 1
        moneyy.money = moneyy.money + pricee.price
        moneyy.save()
        return redirect('main')
        
    else:
        return redirect('main')
        
    
class SignIn(LoginView):
    template_name = 'app/login.html'
    form_class = AuthorizationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)

        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        return self.success_url