from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from aluraflix.models import Category, Video

class CategoryTest(TestCase):
    fixtures = ["test_categories", "initial_database"]
    
    def setUp(self) -> None:
        self.category = Category.objects.get(pk=1)
        self.category_2 = Category.objects.create(
            title="GAMES",
            color="RED"
        )
        self.video = Video.objects.create(
            title="Game Video 1",
            description="Game Video for test",
            url="http://GameVideoTest.com",
            category_id=self.category_2
        )
        
        self.video_2 = Video.objects.create(
            title="Game Video 2",
            description="Game Video 2 for test",
            url="http://GameVideoTest2.com",
            category_id=self.category_2
        )
        return super().setUp()
    
    def test_get_all_category_videos(self):
        
        response = self.client.get(self.category.get_absolute_url()+"videos/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 9)
        
        
        response = self.client.get(self.category_2.get_absolute_url()+"videos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
        