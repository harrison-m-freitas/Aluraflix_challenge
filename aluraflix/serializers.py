from rest_framework import serializers

from aluraflix.models import Video, Category
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', "color"]
      
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', "description", "url", "category_id"]