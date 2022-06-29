from rest_framework import routers
from .views import BrandViewSet, ProductViewSet, ItemViewSet, OrderViewSet


router = routers.DefaultRouter()
router.register('brands', BrandViewSet, basename='brands')
router.register('products', ProductViewSet, basename='products')
router.register('items', ItemViewSet, basename='items')
router.register('orders', OrderViewSet, basename='orders')
urlpatterns = router.urls

