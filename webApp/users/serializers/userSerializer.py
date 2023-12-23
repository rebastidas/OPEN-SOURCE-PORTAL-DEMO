from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'is_staff',
            'is_superuser',
            'is_active',
            'last_login',
            'date_joined',
        ]