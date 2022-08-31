from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import BlogSerializer, CommentSerializer, LikeSerializer
from .permissions import isWritterOrReadOnly
from .models import BlogModel, CommentModel, LikeModel
from .choices import BLOG_TYPES


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userIsWritter(request):
    return Response(request.user.is_writter == True, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def accessToCrudFunctionalityOnBlogId(request, blogId):
    try:
        query = BlogModel.objects.get(id=blogId)
    except Exception as e:
        return Response({'err': 'Blog doest exist'}, status=status.HTTP_404_NOT_FOUND)
    return Response(request.user == query.writter, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, isWritterOrReadOnly])
def blogView(request):
    if request.method == 'GET':
        queryset = BlogModel.objects.all().order_by("-createdAt")
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
def blogDetailView(request, pk, *args, **kwargs):
    try:
        query = BlogModel.objects.get(id=pk)
    except Exception as e:
        return Response({'err': 'blog does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # has_obj_permission doest work on function based views hence i created a check object permission explicitly
    elif query.writter != request.user:
        return Response({'msg': 'You are not authorized'}, status=status.HTTP_403_FORBIDDEN)

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
def likeView(request, blogId):
    if request.method == 'GET':
        try:
            blogStatus = BlogModel.objects.get(id=blogId)

            query = LikeModel.objects.filter(
                blog__id=blogId, is_liked=True).count()
            context = {'likes': query}
            return Response(context, status=status.HTTP_200_OK)
        except Exception:
            return Response({'err': 'blog does not exits'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        query = BlogModel.objects.filter(id=blogId)
        if query:
            serializer = LikeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, blog=query[0])
                # print(serializer.validated_data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'msg': 'incorrect blogId id'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def commentView(request, blogId):
    queryset = CommentModel.objects.filter(blog__id=blogId)
    serializer = CommentSerializer(queryset, many=True)
    if request.method == 'GET':
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        blogQuery = BlogModel.objects.filter(id=blogId)[0]
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
def commentDetailView(request, commentId):
    query = CommentModel.objects.filter(id=commentId)[0]
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


@api_view(['GET'])
@permission_classes([IsAuthenticated, isWritterOrReadOnly])
def getBlogTypeView(request):
    return Response(BLOG_TYPES, status=status.HTTP_200_OK)
