from django.urls import include, path
from rest_framework import routers
from voting import views

router = routers.DefaultRouter()
router.register(r'position', views.PositionViewSet, basename = 'position')
router.register(r'candidate', views.CandidateViewSet, basename = 'candidate')
router.register(r'voter', views.VoterViewSet, basename = 'voter')
router.register(r'votes', views.VotesViewSet, basename = 'votes')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
