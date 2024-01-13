from rest_framework import serializers

from aluraflix.models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', "description", "url"]