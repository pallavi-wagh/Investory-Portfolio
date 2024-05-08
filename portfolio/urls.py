from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('show_investments/', show_investments, name='show_investments'),
    path('show_plan/<int:id>/', description, name='show_plan'),
    path('payment_page/<int:id>/', payment, name='payment_page'),
]

