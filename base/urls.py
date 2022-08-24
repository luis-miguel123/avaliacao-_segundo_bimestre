from operator import concat
from django import views
from django.urls import path
from base.views import indexView

urlpatterns = [
    
    path('index/', indexView.as_view())
]