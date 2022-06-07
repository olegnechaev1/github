from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import CarBrend, CarEngine, CarListing, CarModel
from.forms import CarBrendform, CarModelform, CarEngineform, CarListingform
from django.db.models.functions import Now


class CarBrendCreateView(CreateView):
    model = CarBrend
    template_name = 'cars.html'
    form_class = CarBrendform
    success_url = reverse_lazy('cars')
    
    def get_success_url(self):
        return self.success_url
    
    
class CarModelCreateView(CreateView):
    model = CarModel
    template_name = 'cars_model.html'
    form_class = CarModelform
    success_url = reverse_lazy('carsmodel')
    
    def get_success_url(self):
        return self.success_url    


class CarEngineCreateView(CreateView):
    model = CarEngine
    template_name = 'engine.html'
    form_class = CarEngineform
    success_url = reverse_lazy('engine')
    
    def get_success_url(self):
        return self.success_url


class CarListingCreateView(CreateView):
    model = CarListing
    template_name = 'carListing.html'
    form_class = CarListingform
    success_url = reverse_lazy('list')
    
    def get_success_url(self):
        return self.success_url
    
    
class CarListingListView(ListView):
    model = CarListing
    template_name = 'list.html'
    context_object_name = 'carListing_list'
    queryset = CarListing.objects.filter(date__gte=Now())
    success_url = reverse_lazy('carListing')
    
    def get_success_url(self):
        return self.success_url    
    