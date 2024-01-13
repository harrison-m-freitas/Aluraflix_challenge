from rest_framework import viewsets


from aluraflix.models import Video
from aluraflix.serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer