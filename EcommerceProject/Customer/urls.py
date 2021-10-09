from django.urls import path
from . import views


urlpatterns=[
    path('',views.homeview, name='home'),
    path('seller_to_customer_home', views.seller_to_customer_home, name='seller_to_customer_home'),

    path('showlaptop/',views.showlaptop, name='showlaptop'),
    path('showmobile/', views.showMobile, name='showmobile'),
    path('showgrocery/', views.showGrocery, name='showgrocery'),
    path('customerlaptopitem/<int:pk>', views.Laptopview, name='customerlaptopitem'),
    path('customermobileitem/<int:pk>', views.Mobileview, name='customermobileitem'),
    path('customergroceryitem/<int:pk>', views.Groceryview, name='customergroceryitem'),

    path('cartview/', views.Cartview, name='cartview'),
    path('deleteitem/<int:pk>', views.Deleteitemview, name='deleteitem'),
    path('customerupdateitem/<int:pk>', views.Updateallitemview, name='customerupdateitem'),

]
