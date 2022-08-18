from rest_framework import serializers
from .models import WritterModel


class WritterSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = WritterModel
        fields = ['isStaff','user_name' ]
