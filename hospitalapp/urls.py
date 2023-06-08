from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('lgout',views.lgout,name='lgout'),
    path('dt',views.dt,name='dt'),
    path('services',views.services,name="services"),
    path('lg',views.lg,name='lg'),
    path('about',views.about,name='about'),

]