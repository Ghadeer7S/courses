from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .models import Episode, Podcast, Script, Student, Vocabulary
from .serializers import StudentSerializer, PodcastSerializer, EpisodeSerializer, ScriptSerializer, VocabularySerializer

# class StudentViewSet(ModelViewSet):
#     serializer_class = StudentSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]
    
#     def get_queryset(self):
#         return Student.objects.filter(user=self.request.user)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
        
#     @action(detail=False, methods=['get', 'put'])
#     def me(self, request):
#         (student, created) = Student.objects.get_or_create(user=request.user)
#         if request.method == 'GET':
#             serializer = self.get_serializer(student)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = self.get_serializer(student, data=request.data, partial=True)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
        

class PodcastViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    
class EpisodeViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = EpisodeSerializer
    
    def get_queryset(self):
        podcast_id = self.kwargs['podcast_pk']
        return Episode.objects.filter(podcast_id=podcast_id)
    
class ScriptViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ScriptSerializer
    
    def get_queryset(self):
        episode_id = self.kwargs['episode_pk']
        return Script.objects.filter(episode_id=episode_id)
    
class VocabularyViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = VocabularySerializer
    
    def get_queryset(self):
        episode_id = self.kwargs['episode_pk']
        return Vocabulary.objects.filter(episode_id=episode_id)