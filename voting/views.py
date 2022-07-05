from django.shortcuts import render
from django.contrib.auth.models import *
from rest_framework import viewsets
from rest_framework import permissions
from voting.serializers import *

# Create your views here.
class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows position to be viewed or edited.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]


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


class VoterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows voters to be viewed or edited.
    """
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    permission_classes = [permissions.IsAuthenticated]


class VotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows votes to be viewed or edited.
    """
    queryset = Votes.objects.all()
    serializer_class = VotesSerializer
    permission_classes = [permissions.IsAuthenticated]

