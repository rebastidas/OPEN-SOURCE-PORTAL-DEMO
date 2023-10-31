from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

class ExampleView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        if request.user.is_authenticated:
            return Response({"message": "This is a secured view. You are authenticated."})
        else:
            raise AuthenticationFailed("You are not authenticated.")