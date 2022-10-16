from django.urls import path

from .views import (EconomicPageView, FavoritesPageView, FilmPageView,
                    HomePageView,CommentCreateView, ItPageView, MyprojectLoginView,
                    MyprojectLogout, PoliticPageView, RegistrUserView,
                    SearchView, SportPageView, favorite_project,
                    remove_favorite, like_comment)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('comment', CommentCreateView.as_view(), name='comment'),
    path('sport', SportPageView.as_view(), name='sport'),
    path('politic', PoliticPageView.as_view(), name='politic'),
    path('film', FilmPageView.as_view(), name='film'),
    path('econonic', EconomicPageView.as_view(), name='economic'),
    path('it', ItPageView.as_view(), name='it'),
    path('login', MyprojectLoginView.as_view(), name='login_page'),
    path('register', RegistrUserView.as_view(), name='register_page'),
    path('favorites', FavoritesPageView.as_view(), name='favorites'),
    path('favorites', FavoritesPageView.as_view(), name='favorites'),
    path('search', SearchView.as_view(), name='search'),
    path('logout', MyprojectLogout.as_view(), name='logout_page'),
    path('<id>/favorite_album/', favorite_project, name='favorite_project'),
    path('<id>/remove/', remove_favorite, name='remove'),
    path('like', like_comment, name='like-comment'),
    
]
