from django.urls import path
from . import views
from django.db import models
urlpatterns = [
    path('',views.index,name='index'),
    path('marks/',views.marks,name='marks'),
    path('user/',views.login,name='check'),
    path('login/',views.adminlog,name='login'),
    path('actionbar/',views.action,name='action'),
    path('actionbar/add/',views.add,name='add'),
    path('actionbar/delete/<Reg>',views.delete,name='delete'),
]