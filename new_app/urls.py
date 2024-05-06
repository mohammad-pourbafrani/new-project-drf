from django.urls import path
from . import views

urlpatterns = [
    path("new_api", views.hello_word),
    path("cls", views.HelloWord.as_view()),
    path("ser", views.Users.as_view()),
    path("articles", views.ArticleListView.as_view()),
    path("articles/<int:pk>", views.ArticleDetailView.as_view()),
    path("articles/add", views.AddArticleView.as_view()),
    path("articles/update/<int:pk>", views.UpdateArticle.as_view()),
    path("articles/delete/<int:pk>", views.DeleteArticle.as_view()),
]
