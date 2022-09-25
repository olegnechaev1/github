import factory
from .models import Brand


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
    
    name = factory.Sequence(lambda n: 'name %d' % n)
