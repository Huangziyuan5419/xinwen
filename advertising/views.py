
from rest_framework.response import Response
from rest_framework.views import APIView

from advertising.models import Advertising

from .serializers import AdvertisingSerializer

from utils.response_data import ResponseData


class AdvertisingView(APIView):
    '''广告轮播图'''

    def get(self, request):
        qs = Advertising.objects.all()
        serializer = AdvertisingSerializer(instance=qs, many=True)
        result = ResponseData(serializer.data).return_right()
        return Response(result)


