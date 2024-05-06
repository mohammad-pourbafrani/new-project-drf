from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article


# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=70)
#     last_name = serializers.CharField(max_length=50)
#     email = serializers.EmailField(max_length=100)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=50)
#     body = serializers.CharField()
#     status = serializers.BooleanField()

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(write_only=True)

    class Meta:
        model = Article
        fields = ("id", "title", "body", "status")
        read_only_fields = ["id"]
