from django.urls import path
from.views import like_film 
from films import views

urlpatterns = [
    path('', views.FilmCreateView.as_view(), name='films'),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('registr', views.RegistrUserView.as_view(), name='registr_page'),
    path('logout', views.MyprojectLogout.as_view(), name='logout_page'),
    path('like', like_film, name='like-film'),
] 
