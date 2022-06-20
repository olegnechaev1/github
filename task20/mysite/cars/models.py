from django.db import models


Brend = (
    ('', 'Ваш выбор...'),
    ('Audi', 'Audi'),
    ('Bmw', 'Bmw'),
    ('Mersedes', 'Mersedes')
)
 

class CarBrend(models.Model):
    car_brend = models.CharField(choices=Brend, default='Ваш выбор...', max_length=150, blank=True, null=True)
    
    def __str__(self):
        return str(self.car_brend)
    
    
Model = (
    ('', 'Ваш выбор...'),
    ('седан', 'седан'),
    ('универсал', 'универсал'),
    ('хэтчбэк', 'хэтчбэк'),
    ('джип', 'джип')
)

Drive = (
    ('', 'Ваш выбор...'),
    ('полный', 'полный'),
    ('передний', 'передний'),
    ('задний', 'задний'),
) 
   
    
class CarModel(models.Model):
    car_model = models.CharField(choices=Model, default='Ваш выбор...', max_length=150, blank=True, null=True)
    car_drive = models.CharField(choices=Drive, default='Ваш выбор...', max_length=150, blank=True, null=True)
   
    def __str__(self):
        return f'{self.car_model},{self.car_drive}'
    
    
Engine = (
    ('', 'Ваш выбор...'),
    ('2.0 бензин', '2.0 бензин'),
    ('3.0 бензин', '3.0 бензин'),
    ('2.0 дизель', '2.0 дизель'),
    ('3.0 дизель', '3.0 дизель'),
)    


Year = (
    ('', 'Ваш выбор...'),
    ('2000-20010гг', '2000-20010гг'),
    ('2010-2015гг', '2010-2015гг'),
    ('2015-2020гг', '2015-2020гг'),
    ('2020-2022гг', '2020-2022гг'),
)       
   

class CarEngine(models.Model):
    car_engine = models.CharField(choices=Engine, default='Ваш выбор...', max_length=150, blank=True, null=True)
    year = models.CharField(choices=Year, default='Ваш выбор...', max_length=150, blank=True, null=True)
    
    def __str__(self):
        return f'{self.car_engine}, {self.year}' 
    

class CarListing(models.Model):
    car_brend = models.ForeignKey(CarBrend, on_delete=models.CASCADE, related_name='carBrend')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='carModel')            
    car_engine = models.ForeignKey(CarEngine, on_delete=models.CASCADE, related_name='carEngine')
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.car_brend}, {self.car_model}, {self.car_engine},{self.date}'
    