
from django.urls import path

from . import views


urlpatterns = [
    
    #path to land the homepage
    path('', views.store, name='store'), # '' blank means after store nothing else to display 
    path('<slug:category_slug>/', views.store, name='products_by_category'), # slug for store to get ccategories 
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

] 
