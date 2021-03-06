from django.contrib import messages
from django.shortcuts import redirect, render
from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm, SellerCreationForm
from django.contrib.auth import authenticate, login, logout


def customer_registerview(request):
    form = CustomerCreationForm()
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customerlogin')
    template_name = 'Accounts/register.html'
    context = {'form': form}
    return render(request, template_name, context)


def customer_loginview(request):
    if request.method == 'POST':
        no = request.POST.get('mobile')
        p = request.POST.get('password')
        user = authenticate(username=no, password=p)
        if user and user.is_customer:
            login(request, user)
            return redirect('home')
        messages.error(request, 'You are not a customer')
    template_name = 'Accounts/login.html'
    context = {}
    return render(request, template_name, context)


def seller_registerview(request):
    form = SellerCreationForm()
    if request.method == 'POST':
        form = SellerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sellerlogin')
    template_name = 'Accounts/sellerregister.html'
    context = {'form': form}
    return render(request, template_name, context)


def seller_loginview(request):
    if request.method == 'POST':
        no = request.POST.get('mobile')
        p = request.POST.get('password')
        user = authenticate(username=no, password=p)
        if user and user.is_seller:
            login(request, user)
            return redirect('addproduct')
        messages.error(request, 'You are not a Seller')
    template_name = 'Accounts/SellerLogin.html'
    context = {}
    return render(request, template_name, context)


# def seller_showview(request):
#     usr=Seller.objects.all()
#     print(usr)
#     tempalte_name='Accounts/SellerShow.html'
#     context={'user':usr}
#     return render(request,tempalte_name,context)

def customer_logout_view(request):
    logout(request)
    return redirect('home')


def seller_logout_view(request):
    logout(request)
    return redirect('sellerhome')