from json import JSONDecodeError
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        r = requests.post('http://localhost:8000/api/token/',data = data)
        
        if not r.content:
            return Response({'error': 'Empty response'}, status = r.status_code)
        try:
            return Response(r.json())
        except JSONDecodeError as e:
            print(r.content)
            return Response({'error': f'Failed to decode JSON: {str(e)}'}, status=r.status_code)
        