from rest_framework import serializers
from ..models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email','name', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        user = User(email = self.validated_data['email']) # type: ignore
        password = self.validated_data['password'] # type: ignore
        password2 = self.validated_data['password2'] # type: ignore
        if password != password2:
            raise serializers.ValidationError({'error':'Passwords must match'})
        user.set_password(password)
        user.save()
        return user
    