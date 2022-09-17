from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

# router = SimpleRouter()
router = DefaultRouter()

router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

#     = [
#     path('products/', views.ProductList.as_view(), name='product-list'),
#     path('products/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),

#     path('collections/', views.CollectionList.as_view(), name='collection-list'),
#     path('collections/<int:pk>', views.CollectionDetail.as_view(), name='collection-detail'),
# ]
