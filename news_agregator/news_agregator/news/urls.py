from .views import PoliticPageView, FilmPageView, EconomicPageView
from .views import HomePageView, SportPageView, ItPageView, FavoritesPageView
from .views import MyprojectLoginView, RegistrUserView, MyprojectLogout
from .views import favorite_project, remove_favorite, Search
from django.urls import path


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('sport', SportPageView.as_view(), name='sport'),
    path('politic', PoliticPageView.as_view(), name='politic'),
    path('film', FilmPageView.as_view(), name='film'),
    path('econonic', EconomicPageView.as_view(), name='economic'),
    path('it', ItPageView.as_view(), name='it'),
    path('login', MyprojectLoginView.as_view(), name='login_page'),
    path('register', RegistrUserView.as_view(), name='register_page'),
    path('<id>/favorite_album/', favorite_project, name='favorite_project'),
    path('<id>/remove/', remove_favorite, name='remove'),
    path('favorites', FavoritesPageView.as_view(), name='favorites'),
    path('favorites', FavoritesPageView.as_view(), name='favorites'),
    path('search', Search.as_view(), name='search'),
    path('logout', MyprojectLogout.as_view(), name='logout_page'),
    
]
