from django.urls import path, include
from likes import views

app_name = 'likes'

urlpatterns = [    
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_view()),
    
]



