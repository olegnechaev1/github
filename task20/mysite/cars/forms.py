from django import forms
from .models import CarBrend, CarModel, CarEngine, CarListing


class CarBrendform(forms.ModelForm):
    class Meta:
        model = CarBrend
        fields = ('car_brend',)
        
        
class CarModelform(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ('car_model', 'car_drive')
        
        
class CarEngineform(forms.ModelForm):
    class Meta:
        model = CarEngine
        fields = ('car_engine', 'year')


class CarListingform(forms.ModelForm):
    class Meta:
        model = CarListing
        fields = ('car_brend', 'car_model', 'car_engine')
        