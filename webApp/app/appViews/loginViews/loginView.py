from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        r = requests.post('http://localhost:8000/api/token/',data = data)
        return Response(r.json()) 
        