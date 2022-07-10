from django.shortcuts import render
from django.contrib.auth.models import *
from rest_framework import viewsets
from rest_framework import permissions
from voting.serializers import *
# from rest_framework.decorators import APIView
# from rest_framework.views import APIView

# Create your views here.


# @api_view(['GET','PUT', 'POST', 'DELETE'])
class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows position to be viewed or edited.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]


# @api_view(['GET', 'PUT', 'POST', 'DELETE'])
class CandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows candidates to be viewed or edited.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAuthenticated]


# class RegisterVoterApi(generic.GenerateApiView):
#     serializer_class = CustomVoterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data_request.data)
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validate_data

# @api_view(['GET', 'PUT', 'POST', 'DELETE'])
class VoterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows voters to be viewed or edited.
    """
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    permission_classes = [permissions.IsAuthenticated]


# @api_view(['GET', 'PUT', 'POST', 'DELETE'])
class VotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows votes to be viewed or edited.
    """
    queryset = Votes.objects.all()
    serializer_class = VotesSerializer
    permission_classes = [permissions.IsAuthenticated]

