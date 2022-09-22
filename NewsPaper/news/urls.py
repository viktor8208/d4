from django.urls import path

from .views import (PostList, PostDetail, PostFilterList, PostCreate,
                    PostUpdate, PostDelete)

urlpatterns = [

   path('', PostList.as_view(), name='news'),

   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('search/', PostFilterList.as_view(), name='search'),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),


]
