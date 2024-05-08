from django.shortcuts import render, HttpResponse,redirect
from django.urls import reverse
from .models import *
import razorpay
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def Home(request):
    return render(request, 'portfolio/home.html')

@login_required
def show_investments(request):
    data= Investment.objects.all()
    return render(request, 'portfolio/invest_details.html', context={'data':data})

def description(request, id):
    data=Investment.objects.get(id=id)
    return render(request, 'portfolio/plan_details.html', context={'data':data})

def payment(request, id):
    data=Investment.objects.get(id=id)
    client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    payment = client.order.create({'amount': data.payment_price * 100, 'currency': 'INR', 'payment_capture': 1})
    data.razor_pay_order_id = payment['id']
    data.save()

    return render(request, 'portfolio/payment.html', context={'data': data, 'payment':payment})

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)    

            return redirect(reverse('show_investments'))
    else: 
        return render(request, 'portfolio/login.html')
    

def register_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect(reverse('login'))
        else:
            return HttpResponse('Form is invalid')
        
    else:
        form=UserCreationForm()
        return render(request, 'portfolio/register.html', context={'form':form})
    
def logout_view(request):
    logout(request)
    return render(request,'portfolio/home.html')