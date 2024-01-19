from rest_framework import viewsets, status, generics, filters, renderers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from aluraflix.models import Video, Category
from aluraflix.serializers import VideoSerializer, CategorySerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
    @action(detail=False, name="Free Videos", permission_classes=[])
    def free(self, request, *args, **kwargs):
        queryset = Video.objects.filter(category_id=1)[:5]
        serializer = VideoSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK,  data=serializer.data)
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.description)
    
    def destroy(self, request, *args, **kwargs):
        video = self.get_object()
        v_title = video.title[:25] + (video.title[:25] and ("..."))
        response = Response(status=status.HTTP_204_NO_CONTENT, data={"msg": f"Video '{v_title}' deleted successfully"})
        
        video.delete()
        return response
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

    serializer_class = CategorySerializer
    
    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        c_title = category.title[:25] + (category.title[:25] and ("..."))
        response = Response(status=status.HTTP_204_NO_CONTENT, data={"msg": f"Category '{c_title}' deleted successfully"})
        
        category.delete()
        return response


class VideoCategoryViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer
    
    def get_queryset(self):
        queryset = Video.objects.filter(category_id=self.kwargs['pk'])
        return queryset
