
from django.contrib import admin
from django.urls import path
from exchange.appex.views import bbdc, itub, trpl, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbdc/', bbdc),
    path('itub/', itub),
    path('trpl/', trpl),
    path('', home),
]
