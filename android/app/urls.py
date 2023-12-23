from django.urls import  path
from . import views

urlpatterns = [
    path('', views.App, name='main'),
    path('login/', views.SignIn.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(template_name="app/logout.html"), name='logout'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell')
       
]