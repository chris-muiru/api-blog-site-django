from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import BlogSerializer, CommentSerializer, LikeSerializer
from .permissions import isWritterOrReadOnly
from .models import BlogModel, CommentModel, LikeModel


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
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'GET'])
@permission_classes([IsAuthenticated, isWritterOrReadOnly])
def blogDetaillView(request, pk):
    try:
        query = BlogModel.objects.get(id=pk)
    except Exception as e:
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


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def likeView(request, blogid):
    if request.method == 'GET':
        try:
            blogStatus = BlogModel.objects.get(id=blogid)

            query = LikeModel.objects.filter(
                blog__id=blogid, is_liked=True).count()
            context = {'likes': query}
            return Response(context, status=status.HTTP_200_OK)
        except Exception:
            return Response({'err': 'blog does not exits'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        query = BlogModel.objects.filter(id=blogid)
        if query:
            serializer = LikeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, blog=query[0])
                print(serializer.validated_data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'msg': 'incorrect blogid id'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def commentView(request, blogid):
    queryset = CommentModel.objects.filter(blog__id=blogid)
    serializer = CommentSerializer(queryset, many=True)
    if request.method == 'GET':
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        blogQuery = BlogModel.objects.filter(id=blogid)[0]
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            checkComment = CommentModel.objects.filter(
                comment=serializer.validated_data['comment'])
            if not checkComment:
                serializer.save(user=request.user, blog=blogQuery)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'GET', 'PUT'])
@permission_classes([IsAuthenticated])
def commentDetailView(request, commentid):
    query = CommentModel.objects.filter(id=commentid)[0]
    serializer = CommentSerializer(query)
    if request.method == 'GET':
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CommentSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        query.delete()
        return Response({'comment': 'deleted'}, status=status.HTTP_200_OK)
