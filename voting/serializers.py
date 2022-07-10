from dataclasses import fields
from voting.models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['url', 'name', 'max_vote', 'priority' ]

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ['url', 'fullname', 'image', 'bio', 'position']

# admin??
class VoterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voter
        fields = ['url', 'admin', 'name', 'phone', 'voted', 'verified']
# ('__all__')

class VotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votes
        fields = ['url', 'voter', 'position', 'candidate']

