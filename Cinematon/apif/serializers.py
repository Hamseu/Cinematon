from rest_framework import serializers
from .models import User, Film, Hall, Session, BookedTicket, Cinema

class FilmSerializer(serializers.Serializer):
    film_id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=128)
    imageurl = serializers.CharField(max_length=255)
    genre = serializers.CharField(max_length=128, required=False, allow_null=True, allow_blank=True)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    release_year = serializers.IntegerField()
    length = serializers.IntegerField()
    def create(self, validated_data):
        return Film.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.genre = validated_data.get("genre", instance.genre)
        instance.description = validated_data.get("description", instance.description)
        instance.release_year = validated_data.get("release_year", instance.release_year)
        instance.length = validated_data.get("length", instance.length)
        instance.save()
        return instance

class CinemaSerializer(serializers.Serializer):
    cinemas_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=128)
    city = serializers.CharField(max_length=32)
    street = serializers.CharField(max_length=64)

    def create(self, validated_data):
        return Cinema.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.city = validated_data.get("city", instance.city)
        instance.street = validated_data.get("street", instance.street)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
            password = validated_data.pop("password")
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedTicket
        fields = "__all__"