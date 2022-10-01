from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from news.forms import AuthUserform, CommentForm, RegistrUserform
from news.models import Comment, Like, News


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
        password = form.cleaned_data['password']
        username = form.cleaned_data['username']
        aut_user = authenticate(password=password, username=username)
        login(self.request, aut_user)
        return form_valid
    
    
class MyprojectLogout(LogoutView):
    next_page = reverse_lazy('home')
    
    
class SearchView(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'articles'
    paginate_by = 15        
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        a = "".join(q[0].upper()) + q[1:]
        return News.objects.filter(Q(title__icontains=a) | Q(source__icontains=a))
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class CommentCreateView(generic.CreateView, generic.ListView):
    model = Comment
    template_name = 'comment.html'
    form_class = CommentForm
    context_object_name = 'comment_list'
    success_url = reverse_lazy('comment')

    def get_success_url(self):
        return self.success_url
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        return super(CommentCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        kwargs['comment_list'] = Comment.objects.all().order_by('date') 
        return super().get_context_data(**kwargs)
    
    
def like_comment(request):
    user = request.user 
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment_obj = Comment.objects.get(id=comment_id)
        if user in comment_obj.liked.all():
            comment_obj.liked.remove(user)
        else:
             comment_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, comment_like_id=comment_id)
        if not created:
            if like.value == 'Like':
               like.save()            
    return redirect('comment')


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
