from rest_framework import status

from shops.models import Brand

from .contstants import DEFAULT_BRAND_COUNT


class TestBrend:
    BASE_URL = '/shops/brands/'
    
    def test_get_brends(self, client, create_brands):
        response = client.get(self.BASE_URL)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == Brand.objects.count()
        
    def test_wrong_get_brands(self, client, create_brands):
        response = client.get(self.BASE_URL)
        assert response.status_code != status.HTTP_400_BAD_REQUEST
        assert response.data['count'] != Brand.objects.count() + 1
    
    def test_create_brands(self, client, create_brands):
        data = {
            'name': 'test'
        }
        response = client.post(self.BASE_URL, data)
        assert Brand.objects.count() == DEFAULT_BRAND_COUNT + 1
        assert response.status_code == status.HTTP_201_CREATED
        
    def test_delete_brands(self, client, create_brands):
        response = client.delete('/shops/brands/1/')
        assert Brand.objects.count() == DEFAULT_BRAND_COUNT - 1
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    def test_update_brands(self, client, create_brands):
        data = {
            'name': 'test'
        }
        response = client.put('/shops/brands/1/', data)
        assert Brand.objects.count() == DEFAULT_BRAND_COUNT
        assert response.status_code == status.HTTP_200_OK  
