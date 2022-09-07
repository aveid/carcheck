from rest_framework.views import APIView
from rest_framework import response, status

from mashina.models import Car
from mashina.serializers import CarSerializer


class CarListAPIView(APIView):
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


