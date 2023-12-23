from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from app.models.userProfile import UserProfile
from app.serializers.userProfileSerializer import UserProfileSerializer
from users.models import User
from users.serializers.userSerializer import UserSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request, *args, **kwargs):
        userId = kwargs.get('id')
        user = User.objects.get(id=userId)
        try:
            userProfile = UserProfile.objects.get(user = user)
        except UserProfile.DoesNotExist:
            raise Http404

        serializer = UserProfileSerializer(userProfile)
        return Response({'id':userId, 'data': serializer},status = status.HTTP_200_OK)
    
    def post(self, request):
        email = request.user.email

        try:
            user_instance = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'data': 'User not found'})

        user_serializer = UserSerializer(user_instance)
        user_pk = user_serializer.data['id'] # type: ignore

        if UserProfile.objects.filter(user=user_pk).exists():
            return Response({'message': 'Profile already exists'},status= status.HTTP_400_BAD_REQUEST)
        
        data_to_verify = {**request.data, 'user': user_pk}
        serializer = UserProfileSerializer(data=data_to_verify)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile saved succesfully'})

        return Response({'data': 'data is not valid', 'error': serializer.errors})