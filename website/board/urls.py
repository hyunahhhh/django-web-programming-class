from django.urls import path, re_path

from board import views

app_name = 'board'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    re_path(r'^post/(?P<slug>[-\w]+)$', views.PostDetailView.as_view(), name='post_detail'),
    # tag 관련 추가
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    # search 관련 추가
    path('search/', views.SearchFormView.as_view(), name='search')
]
