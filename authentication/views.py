from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


@api_view(['POST'])
def loginView(request):
    if request.method == "POST":
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not request.user.is_authenticated:
                login(request, user)
                return Response({'msg': 'user successfully logged in'}, status=status.HTTP_200_OK)
            else:
                return Response({'msg': 'already authenticated'}, status=status.HTTP_202_ACCEPTED)
        return Response({"err": "unauthorised"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def registerView(request):
    if request.method == 'POST':
        deserializer = RegisterSerializer(data=request.data)
        if deserializer.is_valid():
            userExist = User.objects.filter(
                username=deserializer.validated_data['username'])
            if not userExist:
                deserializer.save()
        else:
            return Response(deserializer.errors)
    return Response({"msg": "user created"})
