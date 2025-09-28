from django.urls import path
from rest_framework_nested import routers
from .views import  PodcastViewSet, EpisodeViewSet, ScriptViewSet, VocabularyViewSet

router = routers.DefaultRouter()
# router.register('students', StudentViewSet, basename='student')
router.register('podcasts', PodcastViewSet, basename='podcast')

podcast_router = routers.NestedDefaultRouter(router, 'podcasts', lookup='podcast')
podcast_router.register('episodes', EpisodeViewSet, basename='podcast_episodes')

episode_router = routers.NestedDefaultRouter(podcast_router, 'episodes', lookup='episode')
episode_router.register('scripts', ScriptViewSet, basename='episode-scripts')
episode_router.register('vocabulary', VocabularyViewSet, basename='episode-vocabulary')

urlpatterns = router.urls + podcast_router.urls + episode_router.urls