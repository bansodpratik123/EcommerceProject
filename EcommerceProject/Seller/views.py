from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Laptop, Mobile, Grocery
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Accounts.models import CustomUser, Seller
from faker import Faker



# Create your views here.
def homeview(request):
    template_name='Accounts/home.html'
    Laptops=Laptop.objects.all()
    Mobiles=Mobile.objects.all()
    Groceries=Grocery.objects.all()

    context={'Laptops':Laptops, 'Mobiles':Mobiles, 'Groceries':Groceries}
    return render(request,template_name,context)

# CRUD for SELLER-LAPTOP
class LaptopListView(ListView):
    model = Laptop

def AddProductView(request):
    return render(request, 'Seller/AddProduct.html',{} )


class LaptopCreateView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = reverse_lazy('lshow')


def createFakeLaptop(request):
    # if request.method=='POST':
        # no=int(request.POST.get('no'))
        # print(type(no))
        all_user = Seller.objects.all()
        SELLER = []
        for i in all_user:
            print(' All Seller User:', i.user_id, type(i.user_id))
            SELLER.append(i)
        MODEL=['MacBook air 17','MacBook air 2020', 'MacBook Pro', 'VivoNook15', 'Inspiration 3502', 'Notebook Pro', 'Pavilion']
        BRAND = ['HP', 'Apple', 'Dell', 'Asus', 'Lenovo' 'MI']
        RAM=[4,8,12,16, 32]
        ROM=[256,512, 1024, 2048, 4069]
        PROCESSOR=['i3', 'i5', 'i7', 'AMD Ryzen5', 'i9', 'Intel Core 2', 'AMD Ryzen5', 'Intel Atom' ]
        OS=['Windows', 'Linux', 'MackOS']
        WARRANTY=[1,2,3,5,10]
        Price=[50000, 45000, 56000,67000, 15000,50000, 123000 ]

        fake=Faker()
        for i in range(10):
            m=fake.random_element(MODEL)
            b = fake.random_element(BRAND)
            ra = fake.random_element(RAM)
            ro= fake.random_element(ROM)
            pr = fake.random_element(PROCESSOR)
            os=fake.random_element(OS)
            w = fake.random_element(WARRANTY)
            p=fake.random_element(Price)
            se=fake.random_element(SELLER)
            so=fake.random_number(digits=2)
            Laptop.objects.create(seller=se, name=m,brand_name=b, RAM=ra, ROM=ro, processor=pr, OS=os, warranty=w, price=p, stock=so)
        return redirect('lshow')

        return HttpResponse('DAta created')

class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = reverse_lazy('lshow')

class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url = reverse_lazy('lshow')


# CRUD for SELLER-MOBILE
class MobileListView(ListView):
    model = Mobile

class MobileCreateView(CreateView):
    model = Mobile
    fields = '__all__'
    success_url = reverse_lazy('mshow')


def createFakeMobile(request):
    # if request.method=='POST':
        # no=int(request.POST.get('no'))
        # print(type(no))
        all_user = Seller.objects.all()
        SELLER = []
        for i in all_user:
            print(' All Seller User:', i.user_id, type(i.user_id))
            SELLER.append(i)
        MODEL=['Galaxy 12','9A', 'Galaxy M13', 'Note 10S', 'Note M12', 'S 12 Pro']
        BRAND = ['Vivo', 'iphone', 'MI', 'Samsung', 'Realme' 'OPPO']
        RAM=[4,8,12,16]
        ROM=[32,64,128,256,512]
        PROCESSOR=['Quard Core', 'Hexa Core', 'Octa Core', 'SnapDragon']
        WARRANTY=[1,2,3,5,10]
        Price=[23000, 45000, 56000,67000, 15000,50000 ]


        fake=Faker()
        for i in range(10):
            m=fake.random_element(MODEL)
            b = fake.random_element(BRAND)
            ra = fake.random_element(RAM)
            ro= fake.random_element(ROM)
            pr = fake.random_element(PROCESSOR)
            w = fake.random_element(WARRANTY)
            p=fake.random_element(Price)
            s = fake.random_element(SELLER)
            so = fake.random_number(digits=2)
            Mobile.objects.create(seller=s,name=m,brand_name=b, RAM=ra, ROM=ro, processor=pr, warranty=w, price=p, stock=so)
        return redirect('mshow')

        return HttpResponse('DAta created')




class MobileUpdateView(UpdateView):
    model = Mobile
    fields = '__all__'
    success_url = reverse_lazy('mshow')

class MobileDeleteView(DeleteView):
    model = Mobile
    success_url = reverse_lazy('mshow')


# CRUD for SELLER-GROCERY
class GroceryListView(ListView):
    model = Grocery

class GroceryCreateView(CreateView):
    model = Grocery
    fields = '__all__'
    success_url = reverse_lazy('gshow')

def createFakeGrocery(request):
    # if request.method=='POST':
        # no=int(request.POST.get('no'))
        # print(type(no))
        user=request.user
        print(' Seller User for fake data:', user.id)
        all_user=Seller.objects.all()
        SELLER = []
        for i in all_user:
            print(' All Seller User:', i.user_id, type(i.user_id))
            SELLER.append(i)

        NAME=['Sugar','Tea Powder', 'Coffee Powder', 'Chana / Chole', 'Red Rajma','Rosted Suji (Rava)']
        Price=[23, 45, 56]
        WARRANTY = [1, 2, 3, 5, 10]
        print(SELLER)
        fake=Faker()
        for i in range(10):
            n=fake.random_element(NAME)
            q = fake.random_number(digits=2)
            p=fake.random_element(Price)
            w = fake.random_element(WARRANTY)
            s = fake.random_element(SELLER)
            Grocery.objects.create(seller=s, product_name=n,quantity=q, price=p, warranty=w)
        return redirect('gshow')

        return HttpResponse('DAta created')

class GroceryUpdateView(UpdateView):
    model = Grocery
    fields = '__all__'
    success_url = reverse_lazy('gshow')

class GroceryDeleteView(DeleteView):
    model = Grocery
    success_url = reverse_lazy('gshow')


