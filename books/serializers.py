from datetime import datetime

from rest_framework import serializers

from books.models import AuthorModel


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    birthdate = serializers.DateField()

    def create(self, validated_data):
        return AuthorModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    isbn = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    author = AuthorSerializer()

    def create(self, validated_data):
        return AuthorModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



