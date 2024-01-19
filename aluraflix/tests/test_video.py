import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from aluraflix.models import Video

class VideoTest(TestCase):
    video = None
    fixtures = ["initial_database"]
    
    def setUp(self) -> None:
        self.get_video_instance()
        self.list_url = reverse("videos-list")
    
    def test_load_fixtures(self):
        """Testing load fixtures data"""
        video_1 = Video.objects.get(pk=1)
        all_videos = Video.objects.all()
        
        self.assertEqual(video_1.title, "Histórias do Quartel 20 Soldado Bisonho e Capitão!")
        self.assertEqual(len(all_videos), 9)
        
    def test_get_all_video(self):
        """Testing get resquest all videos"""
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 9)
        
    def test_get_video_details(self):
        """Testing get resquest one video details"""
        
        response = self.client.get(self.video.get_absolute_url())
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data_json = response.json()
        self.assertEqual(data_json["title"], self.video.title)
        self.assertEqual(data_json["description"], self.video.description)
        self.assertEqual(data_json["url"], self.video.url)
        
    def test_get_video_search(self):
        """Testing get resquest video filter search"""
        response = self.client.get(self.list_url, data={"search":"Soldado"})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)
        
    def test_add_video(self):
        """Testing post request to add video"""
        
        video = {
            "title": "The Death of Death in the Death of Christ - The Good News of a Bloody Cross (Session IV)",
            "description": "To speak of God’s wrath evokes all different sorts of emotions and reaction in people. Yet the horrific death of Christ and his glorious resurrection is the greatest news that mankind could ever hear given that with each day, humans store up God’s righteous judgment and wrath. Believing this news necessitates announcing it.",
            "url": "https://www.youtube.com/watch?v=bmgewPn9mCI"
        }
        

        response = self.client.post(self.list_url, data=video)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data_json = response.json()

        self.assertEqual(data_json['title'], video['title'])
        self.assertEqual(data_json['description'], video['description'])
        self.assertEqual(data_json['url'], video['url'])
        self.assertEqual(data_json['category_id'], 1)

    def test_update_partial_video_details(self):
        """Testing patch request to update partial details"""
        
        data = {
            "description": "update description"
        }
        
        response = self.client.patch(self.video.get_absolute_url(), data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.get_video_instance()

        self.assertEqual(self.video.description, data['description'])

    def test_update_all_fields_video_details(self):
        """Testing put resquest to update all fields"""
        
        
        data = {
            "title": "Update Title",
            "description": "update description V2",
            "url": "https://updateUrl.com"
        }
        
        response = self.client.put(self.video.get_absolute_url(), data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.get_video_instance()
        
        self.assertEqual(self.video.title, data['title'])
        self.assertEqual(self.video.description, data['description'])
        self.assertEqual(self.video.url, data['url'])
        
    def test_delete_video(self):
        """Testing delete request to delete video"""
        
        response = self.client.delete(self.video.get_absolute_url())

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        self.get_video_instance()
        
        self.assertEqual(self.video, None)
    
    def get_video_instance(self, pk: int = 1):
        try:
            self.video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            self.video = None