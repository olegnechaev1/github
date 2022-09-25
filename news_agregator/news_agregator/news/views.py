from django.views import generic
from django.contrib.auth import authenticate, login
from news.forms import AuthUserform, RegistrUserform
from news.models import News
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q


def favorite_project(request, id):
    if request.method == 'POST':
        news = get_object_or_404(News, pk=id)
        if not news.is_favorite:
            news.is_favorite = True
            news.save()
    return redirect(request.POST.get('url_from'))
    
    
def remove_favorite(request, id):
    if request.method == 'POST':
        news = News.objects.get(pk=id)
        if news.is_favorite:
            news.is_favorite = False
            news.save()
    return redirect('favorites')    


class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'
    paginate_by = 20
    
    def get_queryset(self):
        return News.objects.all()
    
    
class SportPageView(generic.ListView):
    template_name = 'sport.html'
    context_object_name = 'articles'
    paginate_by = 15
    
    def get_queryset(self):
        return News.objects.filter(source='Спорт RSS')
    
    
class PoliticPageView(generic.ListView):
    template_name = 'politic.html'
    context_object_name = 'articles'
    paginate_by = 15
    
    def get_queryset(self):
        return News.objects.filter(source='Политика RSS')
    
    
class FilmPageView(generic.ListView):
    template_name = 'film.html'
    context_object_name = 'articles'
    paginate_by = 15
    
    def get_queryset(self):
        return News.objects.filter(source='Фильм RSS')
    
    
class EconomicPageView(generic.ListView):
    template_name = 'economic.html'
    context_object_name = 'articles'
    paginate_by = 15
    
    def get_queryset(self):
        return News.objects.filter(source='Экономика RSS')
    
    
class ItPageView(generic.ListView):
    template_name = 'it.html'
    context_object_name = 'articles'
    paginate_by = 15
    
    def get_queryset(self):
        return News.objects.filter(source='Хакер RSS')
    

class FavoritesPageView(generic.ListView):
    template_name = 'favorites.html'
    context_object_name = 'articles'
    paginate_by = 15
    
    def get_queryset(self):
        return News.objects.filter(is_favorite=True)    
    
    
class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserform
    success_url = reverse_lazy('home')
    
    def get_success_url(self):
        return self.success_url
    
    
class RegistrUserView(generic.CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegistrUserform
    success_url = reverse_lazy('home')
    
    def get_success_url(self):
        return self.success_url
    
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        password = form.cleaned_data["password"]
        username = form.cleaned_data["username"]
        aut_user = authenticate(password=password, username=username)
        login(self.request, aut_user)
        return form_valid
    
    
class MyprojectLogout(LogoutView):
    next_page = reverse_lazy('home')
    
    
class Search(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'articles'
    paginate_by = 15        
    
    def get_queryset(self):
        q = self.request.GET.get('q').capitalize()
        #a = "".join(q[0].upper()) + q[1:]
        return News.objects.filter(Q(title__icontains=q) | Q(source__icontains=q))
    
    def get_context_data(self, *args, **kwargs):
        contex = super().get_context_data(*args, **kwargs)
        contex['q'] = self.request.GET.get('q')
        return contex
    