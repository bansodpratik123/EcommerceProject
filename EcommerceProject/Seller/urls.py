
from django.urls import path
from .views import LaptopListView, LaptopCreateView, LaptopUpdateView, LaptopDeleteView, AddProductView
from .views import MobileListView, MobileCreateView, MobileDeleteView, MobileUpdateView, homeview
from .views import GroceryListView, GroceryCreateView, GroceryUpdateView, GroceryDeleteView
from . import views

urlpatterns = [
    path('', homeview, name='home'),

    path('addproduct/', AddProductView, name='addproduct'),

    path('lcreate/', LaptopCreateView.as_view(), name='lcreate'),
    path('cfl/', views.createFakeLaptop, name='cfl'),

    path('lshow/', LaptopListView.as_view(), name='lshow'),
    path('lupdate/<int:pk>', LaptopUpdateView.as_view(), name='lupdate'),
    path('ldelete/<int:pk>', LaptopDeleteView.as_view(), name='ldelete'),

    # path('showlaptop', views.showlaptops, name='showlaptop'),

    path('mcreate/', MobileCreateView.as_view(), name='mcreate'),
    path('cfm/', views.createFakeMobile, name='cfm'),

    path('mshow/', MobileListView.as_view(), name='mshow'),
    path('mupdate/<int:pk>', MobileUpdateView.as_view(), name='mupdate'),
    path('mdelete/<int:pk>', MobileDeleteView.as_view(), name='mdelete'),

    path('gcreate/', GroceryCreateView.as_view(), name='gcreate'),
    path('cfg/', views.createFakeGrocery, name='cfg'),

    path('gshow/', GroceryListView.as_view(), name='gshow'),
    path('gupdate/<int:pk>', GroceryUpdateView.as_view(), name='gupdate'),
    path('gdelete/<int:pk>', GroceryDeleteView.as_view(), name='gdelete'),
]