from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from aluraflix.models import Category

class CategoryTest(TestCase):
    category = None
    fixtures = ["test_categories"]
    
    def setUp(self) -> None:
        self.get_category_instance()
        self.list_url = reverse("categories-list")
    
    def test_load_fixtures(self):
        """Testing load fixtures data"""
        category_2 = Category.objects.get(pk=2)
        all_categories = Category.objects.all()
        
        self.assertEqual(category_2.title, "GAMES")
        self.assertEqual(len(all_categories), 5)
        
    def test_get_all_categories(self):
        """Testing get resquest all categories"""
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)
        
    def test_get_category_details(self):
        """Testing get resquest one category details"""
        self.get_category_instance(3)
        response = self.client.get(self.category.get_absolute_url())
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data_json = response.json()
        self.assertEqual(data_json["title"], self.category.title)
        self.assertEqual(data_json["color"], self.category.color)
    
    
    def test_add_category(self):
        """Testing post request to add category"""
        
        category = {
            "title": "LIVES",
            "color": "VIOLET"
        }
        

        response = self.client.post(self.list_url, data=category)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        data_json = response.json()

        self.assertEqual(data_json["title"], category["title"])
        self.assertEqual(data_json["color"], category["color"])

    def test_update_partial_category_details(self):
        """Testing patch request to update partial details"""
        
        data = {
            "color": "update color"
        }
        
        response = self.client.patch(self.category.get_absolute_url(), data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.get_category_instance()

        self.assertEqual(self.category.color, data['color'])

    def test_update_all_fields_category_details(self):
        """Testing put resquest to update all fields"""   
        
        data = {
            "title": "Update Title",
            "color": "update description V2",
        }
        
        response = self.client.put(self.category.get_absolute_url(), data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.get_category_instance()
        
        self.assertEqual(self.category.title, data['title'])
        self.assertEqual(self.category.color, data['color'])
               
    def test_delete_category(self):
        """Testing delete request to delete category"""
        
        response = self.client.delete(self.category.get_absolute_url())

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        self.get_category_instance()
        
        self.assertEqual(self.category, None)
    
    def get_category_instance(self, pk: int = 1):
        try:
            self.category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            self.category = None