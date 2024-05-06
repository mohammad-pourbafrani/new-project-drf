from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, ArticleSerializer
from .models import Article


@api_view(["Get", "POST", "PATCH", "PUT"])
def hello_word(request):
    document = [
        {"name": "mobile", "amount": "1323323", "balance": 123.0, "status": True},
        {"name": "laptop", "amount": "5353232", "balance": 321, "status": False},
    ]
    name = request.GET.get("name")
    last = request.GET.get("last")
    if request.method == "POST":
        return Response({"method": "POST", "name": name, "last": last})
    elif request.method == "GET":
        return Response([document, [{"name": name, "last": last}]])
    elif request.method == "PUT":
        return Response({"method": "PUT"})
    elif request.method == "PATCH":
        return Response({"method": "PATCH"})


class HelloWord(APIView):
    def get(self, request):
        document = [
            {"name": "mobile", "amount": "1323323", "balance": 123.0, "status": True},
            {"name": "laptop", "amount": "5353232", "balance": 321, "status": False},
        ]
        return Response({"name": "class based view hello word", "data": document})

    def post(self, request):
        name = request.data.get("name")
        last = request.data.get("last")
        return Response({"name": f"{name} {last}"})

    def delete(self, request):
        return Response({"name": "fucking request "})


class Users(APIView):
    def get(self, request):
        idName = request.GET.get("id")
        queryset = User.objects.get(id=idName)
        ser = UserSerializer(instance=queryset)
        return Response(data=ser.data)


class ArticleListView(APIView):
    def get(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)


class ArticleDetailView(APIView):
    def get(self, request, pk):
        instance = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=instance)
        return Response(serializer.data)


class AddArticleView(APIView):
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UpdateArticle(APIView):
    def put(self, request, pk):
        instance = Article.objects.get(id=pk)
        serializer = ArticleSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(instance=instance , validated_data=serializer.validated_data)
            return Response({"message":"updated"})
        return Response(serializer.errors)

class DeleteArticle(APIView):
    def delete(self , request , pk):
        instance = Article.objects.get(id=pk)
        instance.delete()
        return Response({"message":"deleted"})