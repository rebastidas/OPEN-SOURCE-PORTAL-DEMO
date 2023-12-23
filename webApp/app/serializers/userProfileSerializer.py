from rest_framework import serializers
from app.models.userProfile import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def is_valid(self, raise_exception = False):
        valid = super().is_valid(raise_exception = raise_exception)
        return valid

    