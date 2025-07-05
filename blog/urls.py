from django.urls import path
from blog.views import *

urlpatterns = [
    path('', ArticleView.as_view(), name='home'),
    path('categories/<int:pk>', ArticleByCategory.as_view(), name='category'),
    path('search/', SearchQuery.as_view(), name='search'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='detail'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('add_article/', AddArticle.as_view(), name='create'),
    path('update_article/<int:pk>/', UpdateArticle.as_view(), name='update'),
    path('delete_article/<int:pk>/', DeleteArticle.as_view(), name='delete'),
    path('add_comment/<int:pk>/', add_comment, name='comment'),
]
