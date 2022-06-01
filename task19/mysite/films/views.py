from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Film, Like
from.forms import AuthUserform, RegistrUserform, Filmsform
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

User = get_user_model()

  
def like_film(request):
    user = request.user 
    if request.method == 'POST':
        film_id = request.POST.get('film_id')
        film_obj = Film.objects.get(id=film_id)
        if user in film_obj.liked.all():
            film_obj.liked.remove(user)
        else:
             film_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, film_id=film_id)
        if not created:
            if like.value == 'Like':
               like.value = 'Like'
               like.save()            
    return redirect('films')


class FilmCreateView(CreateView, ListView):
    login_url = reverse_lazy('login_page')
    model = Film
    template_name = 'info.html'
    form_class = Filmsform
    context_object_name = 'film_list'
    success_url = reverse_lazy('films')

    def get_context_data(self, **kwargs):
        kwargs['film_list'] = Film.objects.all().order_by('date') 
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    
class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserform
    success_url = reverse_lazy('films')
    
    def get_success_url(self):
        return self.success_url
    
    
class RegistrUserView( CreateView):
    model = User
    template_name = 'registr.html'
    form_class = RegistrUserform
    success_url = reverse_lazy('films')
    
    def get_success_url(self):
        return self.success_url
    
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        password = form.cleaned_data["password"]
        email = form.cleaned_data["email"]
        aut_user = authenticate(password=password, email=email)
        login(self.request, aut_user)
        return form_valid
    
    
class MyprojectLogout(LogoutView):
    next_page = reverse_lazy('films')    

