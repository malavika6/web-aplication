from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.signup,name="signup"),
    path('signin1',views.signin,name="signin1"),
    path('home',views.home,name="home"),
    path('signout',views.signout,name="signout"),
    path('add',views.add,name="add"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('/<int:id>',views.update,name="update"),

]