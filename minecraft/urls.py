from django.urls import path

from . import views
from . import models


app_name = "minecraft"
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('createAccount/', views.CreateAccountView.as_view(), name='createAccount'),
    path('resetPassword/', views.ResetPasswordView.as_view(), name='resetPassword'),
    path('post/', views.PostView.as_view(), name='post'),
    path('postImage/', views.PostImageView.as_view(), name='postImage'),
    path('postThread/', views.PostThreadView.as_view(), name='postThread'),
    path('postMod/', views.PostModView.as_view(), name='postMod'),
    path('main/', views.MainView.as_view(), name='main'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('searchMod/', views.SearchModView.as_view(), name='searchMod'),
    path('searchPhoto/', views.SearchPhotoView.as_view(), name='searchPhoto'),
    path('userInfo/', views.UserInfoView.as_view(), name='userInfo'),
    # path('searchPhoto/<str:pk>/', views.SearchPhotoView.as_view(), name='likes_img'),#コメントのほう？
    # path('like_for_post/', views.like_for_post, name='like_for_post'),
    # path('like/', views.like, name='like'),
    path('searchThread/', views.SearchThreadView.as_view(), name='searchThread'),
	path('searchThread/<str:pk>/', views.post_thread_list, name='Thread'),
    path('setting/', views.SettingView.as_view(), name='setting'),
    path('released/', views.ReleasedView.as_view(), name='released'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]