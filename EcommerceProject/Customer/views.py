from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Accounts.models import Customer
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Seller.models import Laptop, Mobile, Grocery
from .filters import LaptopFilter, MobileFilter, GroceryFilter



# Create your views here.
def seller_to_customer_home(request):
    logout(request)
    return redirect('home')
    # template_name='Customer/Customer_Home.html'
    # Laptops=Laptop.objects.all()
    # Mobiles=Mobile.objects.all()
    # Groceries=Grocery.objects.all()
    #
    # context={'Laptops':Laptops, 'Mobiles':Mobiles, 'Groceries':Groceries}
    # return render(request,template_name,context)


def homeview(request):
    template_name='Customer/Customer_Home.html'
    Laptops=Laptop.objects.all()
    Mobiles=Mobile.objects.all()
    Groceries=Grocery.objects.all()

    context={'Laptops':Laptops, 'Mobiles':Mobiles, 'Groceries':Groceries}
    return render(request,template_name,context)


def showlaptop(request):
    records = Laptop.objects.all()
    laptopfilter = LaptopFilter(request.GET, queryset=records)
    rec_per_page = Paginator(laptopfilter.qs, 3)
    page = request.GET.get('page',1)
    # print('PAGE=',page)
    # print(rec_per_page.count)
    # print(rec_per_page.num_pages)
    # print(rec_per_page.page_range)
    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)
    print('filter record', records)
    return render(request, 'Customer/ShowLaptop.html', {'records': rec, 'laptopfilter': laptopfilter})

def showMobile(request):
    records = Mobile.objects.all()
    mobilefilter = MobileFilter(request.GET, queryset=records)
    rec_per_page = Paginator(mobilefilter.qs, 5)
    print('PAGINATOR=', rec_per_page)

    page=request.GET.get('page',1)
    print('PAGE=',page)
    print(rec_per_page.count)
    print(rec_per_page.num_pages)
    print(rec_per_page.page_range)

    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)

    return render(request,'Customer/ShowMobile.html',{'records':rec, 'mobilefilter':mobilefilter})

def showGrocery(request):
    records = Grocery.objects.all()
    groceryfilter = GroceryFilter(request.GET, queryset=records)
    rec_per_page = Paginator(groceryfilter.qs, 3)
    print('PAGINATOR=', rec_per_page)

    page=request.GET.get('page',1)
    print('PAGE=',page)
    print(rec_per_page.count)
    print(rec_per_page.num_pages)
    print(rec_per_page.page_range)

    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)

    return render(request,'Customer/ShowGrocery.html',{'records':rec, 'groceryfilter':groceryfilter})

@login_required(login_url='customerlogin')
def Laptopview(request, pk):
    laptop = Laptop.objects.get(id=pk)
    user = request.user
    print('User :',user.id)
    cst = Customer.objects.get(user=user)
    y = Cart.objects.filter(customer=cst, laptop=laptop).first()
    if y:
        z = y.quantity + 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('cartview')
    else:
        Cart.objects.create(customer=cst, laptop=laptop, mobile=None, grocery=None, price=laptop.price, quantity=1)
        print('Created!!!')
    return redirect('cartview')

@login_required(login_url='customerlogin')
def Mobileview(request, pk):
    mobile = Mobile.objects.get(id=pk)
    user = request.user
    cst = Customer.objects.get(user=user)
    y = Cart.objects.filter(customer=cst, mobile=mobile).first()
    if y:
        z = y.quantity + 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('cartview')
    else:
        Cart.objects.create(customer=cst, laptop=None, mobile=mobile, grocery=None, price=mobile.price, quantity=1)
        print('Created!!!')
    return redirect('cartview')

@login_required(login_url='customerlogin')
def Groceryview(request, pk):
    grocery = Grocery.objects.get(id=pk)
    user = request.user
    cst = Customer.objects.get(user=user)
    y = Cart.objects.filter(customer=cst, grocery=grocery).first()
    if y:
        z = y.quantity + 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('cartview')
    else:
        Cart.objects.create(customer=cst, laptop=None, mobile=None, grocery=grocery, price=grocery.price, quantity=1)
        print('Created!!!')
    return redirect('cartview')


@login_required(login_url='customerlogin')
def Cartview(request):
    user = request.user
    # print('User:', user)
    cst = Customer.objects.get(user=user)
    print(cst)
    ord = Cart.objects.filter(customer=cst)
    for i in ord:
        if i.laptop_id is not None:
            product_id = i.laptop_id
            product_name_l = Laptop.objects.get(id=product_id)
            print("Laptop", product_name_l.name)
        elif i.mobile_id is not None:
            product_id = i.mobile_id
            product_name_m = Mobile.objects.get(id=product_id)
            print("Mobile", product_name_m.name)
        elif i.grocery_id is not None:
            product_id = i.grocery_id
            product_name_g = Grocery.objects.get(id=product_id)
            print("Mobile", product_name_g)
            print(product_id)
    template_name = 'Customer/showCart.html'
    context = {'ord': ord, 'product_name_m': product_name_m.name, 'product_name_l': product_name_l.name,'product_name_g':product_name_g}
    return render(request, template_name, context)


@login_required(login_url='login')
def Deleteitemview(request, pk):
    # item=Order_item.objects.get(id=pk)
    # item.delete()
    # return redirect('cartview')
    y = Cart.objects.get(id=pk)
    if y.quantity > 1:
        z = y.quantity - 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('cartview')
    else:
        print('Deleted!!')
        y.delete()
    return redirect('showcart')


def Updateallitemview(request, pk):
    y = Cart.objects.filter(id=pk).first()
    if y:
        z = y.quantity + 1
        p = y.price / y.quantity
        q = p * z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('cartview')

