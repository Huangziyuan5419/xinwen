from rest_framework import serializers

from .models import Advertising


class AdvertisingSerializer(serializers.ModelSerializer):
    '''
    广告序列化
    '''
    class Meta:
        model = Advertising
        fields = '__all__'

