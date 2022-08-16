from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class BlogView(APIView):
    def get(self, request):
        return Response()

# Create your views here.
