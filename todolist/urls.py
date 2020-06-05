"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # Auth
    path('signin/', views.userlogin, name='userlogin'),
    path('signup/', views.usersignup, name='usersignup'),
    path('logout/', views.userlogout, name="userlogout"),

    # todo
    path('currenttodo', views.currenttodo, name='currenttodo'),
    path('createtodo/', views.createtodo, name='createtodo'),
    path('todo/<int:todo_pk>', views.todoview, name='todoview'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/uncomplete', views.uncompletetodo, name='uncompletetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    path('viewcompleted/', views.viewcompleted, name='viewcompleted'),
]
