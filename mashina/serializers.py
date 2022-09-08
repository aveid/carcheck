from rest_framework import serializers

from mashina.models import Car, CarImage, CarOwner


class ImageSerializer(serializers.ModelSerializer):
    id_image = serializers.IntegerField(source='id')

    class Meta:
        model = CarImage
        fields = ("id_image", "image")


class CarOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOwner
        fields = "__all__"


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    model = serializers.CharField(max_length=150)
    year = serializers.DateField()
    engine = serializers.FloatField()
    color = serializers.CharField(max_length=150)
    number = serializers.CharField(max_length=10)
    images = serializers.SerializerMethodField()
    owners = serializers.SerializerMethodField()

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.model = validated_data.get("model", instance.model)
        instance.year = validated_data.get("year", instance.year)
        instance.engine = validated_data.get("engine", instance.engine)
        instance.color = validated_data.get("color", instance.color)
        instance.number = validated_data.get("number", instance.number)
        instance.save()
        return instance

    def get_images(self, obj):
        car_images = CarImage.objects.filter(
            car=obj.id)
        serializer = ImageSerializer(car_images, many=True)

        return serializer.data

    def get_owners(self, obj):
        car_owners = CarOwner.objects.filter(
            car=obj.id)
        serializer = CarOwnerSerializer(car_owners, many=True)

        return serializer.data




