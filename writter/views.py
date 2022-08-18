from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import WritterSerializer
from .models import WritterModel


@api_view(['POST', 'GET'])
def writterView(request):
    writterQuery = WritterModel.objects.all()
    serializer = WritterSerializer(writterQuery, many=True)
    if request.method == 'POST':
        writter_exists = WritterModel.objects.filter(
            user=serializer.data['user'])
        deserializer = WritterSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(serializer.data, status=status.HTTP_200_OK)
