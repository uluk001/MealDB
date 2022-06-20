"""mealdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mealapp.views import main, letter, search, second_site, filter_by_area, search_ingredients, basket, addToCart, removeCart
from mealdb.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('search', search, name="search"),
    path('addToCart/<int:id>', addToCart, name='addToCart'),
    path('search_ingredients', search_ingredients, name="search_ingredients"),
    path('letter/<int:pk>',letter,  name='letter'),
    path('removeCart/<int:id>', removeCart, name='removeCart'),
    path('second_site/<int:pk>', second_site, name="second_site"),
    path('filter_by_area/<int:pk>', filter_by_area,  name='filter_by_area'),
    path('basket', basket, name='basket')

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
