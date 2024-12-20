from django.urls import path
from .views import *


app_name = 'feed'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'), # pk = primary key
    path('post/', AddPostView.as_view(), name='post'), 
    
]
