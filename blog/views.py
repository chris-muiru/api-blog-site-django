from os import stat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import BlogSerializer
from .permissions import isWritterOrReadOnly
from .models import BlogModel


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, isWritterOrReadOnly])
def blogView(request):
    if request.method == 'GET':
        queryset = BlogModel.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            query = BlogModel.objects.filter(
                title=serializer.validated_data['title'])
            if not query:
                serializer.save(writter=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'GET'])
@permission_classes([IsAuthenticated, isWritterOrReadOnly])
def blogDetaillView(request, pk):
    try:
        query = BlogModel.objects.get(id=pk)
        print(query)
    except query.DoesNotExist:
        return Response({'err': 'blog does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BlogSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        query.delete()
        return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)
