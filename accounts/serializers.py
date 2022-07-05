from rest_framework import serializers
from accounts.models import *


class CustomUserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='users-detail')

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'user_type',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

  
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance