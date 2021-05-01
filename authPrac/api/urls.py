from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
# from .views import  RegisterView

urlpatterns = [

    # path('users/', views.UserList.as_view()),
    # path('users/<pk>/', views.UserDetail.as_view()),
    path('articles/', views.ArticlesList.as_view()),
    path('articles/<pk>/', views.ArticlesDetail.as_view()),
    path('comments/', views.CommentsList.as_view()),
    path('comments/<pk>/', views.CommentsDetail.as_view()),
    path('likes/', views.LikesList.as_view()),
    path('likes/<pk>/', views.LikesDetail.as_view()),
    path('media/', views.MediaList.as_view()),
    path('media/<pk>/', views.MediaDetail.as_view()),
    # path('api/register/', RegisterView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)