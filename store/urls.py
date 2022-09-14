from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),

    path('collections/', views.collection_list, name='collection-list'),
    path('collections/<int:pk>', views.collection_detail, name='collection-detail'),

]