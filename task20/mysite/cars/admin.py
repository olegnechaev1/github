from django.contrib import admin
from .models import CarBrend, CarModel, CarEngine, CarListing


class CarListingline(admin.TabularInline):
    model = CarListing


class CarBrendAdmin(admin.ModelAdmin):
    list_display = (
        'car_brend',
    )
    inlines = [
        CarListingline,
    ]
    

class CarModelAdmin(admin.ModelAdmin):
    list_display = (
        'car_model',
        'car_drive',
    ) 


class CarEngineAdmin(admin.ModelAdmin):
    list_display = (
        'car_engine',
        'year',
    )
           

class CarListingAdmin(admin.ModelAdmin):
    list_display = (
        'car_model',
        'car_brend',
        'car_engine',
        'date',
    )
    
    search_fields = ['car_brend__car_brend']
    raw_id_fields = ('car_model', 'car_engine',)


admin.site.register(CarBrend, CarBrendAdmin)    
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarEngine, CarEngineAdmin)
admin.site.register(CarListing, CarListingAdmin)