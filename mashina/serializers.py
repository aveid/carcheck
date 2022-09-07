from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    model = serializers.CharField(max_length=150)
    year = serializers.DateField()
    # engine = serializers.FloatField()
    color = serializers.CharField(max_length=150)
