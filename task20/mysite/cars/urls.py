from django.urls import path
from cars import views

urlpatterns = [
    path('', views.CarListingCreateView.as_view(), name='carListing'),
    path('model', views.CarModelCreateView.as_view(), name='carsmodel'),
    path('engine', views.CarEngineCreateView.as_view(), name='engine'),
    path('cars', views.CarBrendCreateView.as_view(), name='cars'),
    path('list', views.CarListingListView.as_view(), name='list'),
] 