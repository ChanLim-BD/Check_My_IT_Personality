from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('form/', views.form),
    path('submit/', views.submit),
    path('result/<int:developer_id>/', views.result),
]