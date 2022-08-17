from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.permissions import AllowAny


@csrf_protect
@api_view(['POST'])
def LoginView(request):
    if request.method == "POST":
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not request.user.is_authenticated:
                login(request, user)
                return Response({'msg': f'{request.user} successfully logged in'}, status=status.HTTP_200_OK)
            else:
                return Response({'msg': 'already authenticated'}, status=status.HTTP_202_ACCEPTED)
        return Response({"err": "unauthorised"}, status=status.HTTP_401_UNAUTHORIZED)



class RegisterApiView():
    pass


# Create your views here.
