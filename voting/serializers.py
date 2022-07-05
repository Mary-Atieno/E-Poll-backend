from dataclasses import fields
from email.mime import image
from voting.models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['url', 'name', 'max_vote', 'priority' ]

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    # image=CloudinaryField('image')
    class Meta:
        model = Candidate
        fields = ['url', 'fullname', 'image', 'bio']

# admin??
class VoterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voter
        fields = ['url', 'phone', 'otp', 'otp_sent', 'voted', 'verified','name']
# ('__all__')

class VotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votes
        fields = ['url', 'voter', 'position', 'candidate']

