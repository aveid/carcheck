from django.http import Http404
from rest_framework.views import APIView
from rest_framework import response, status

from mashina.models import Car
from mashina.serializers import CarSerializer, ImageSerializer


class CarListAPIView(APIView):

    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return response.Response(serializer.data,
                                 status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED)
        return response.Response(status=status.HTTP_400_BAD_REQUEST)


class DetailCarAPIView(APIView):

    def get_object(self, number):
        try:
            return Car.objects.get(number=number)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, number, format=None):
        car = self.get_object(number)
        serializer = CarSerializer(car)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, number, format=None):
        car = self.get_object(number)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, number, format=None):
        car = self.get_object(number)
        car.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class CreateImageAPIView(APIView):

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED)
        return response.Response(status=status.HTTP_400_BAD_REQUEST)