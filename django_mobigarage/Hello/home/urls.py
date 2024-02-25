from home import views
from django.urls import path

urlpatterns = [
    # path('',views.mini_site, name='mini_site'),
    path('about_us',views.about_us,name= 'about_us'),
    path('price', views.price, name='price'),
    path('brands',views.brand,name='brands'),
    path('rating',views.rating,name= 'rating'),
    path('base',views.base,name= 'base'),
    path('',views.mini_site,name ='mini_site'),
    path('home',views.mini_site,name='home')
]
