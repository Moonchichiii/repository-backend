from django.urls import path, include
from comments import views

app_name = 'comments'

urlpatterns = [    
    #path('comments/', views.CommentList.as_view()),
    #path('comments/<int:pk>/', views.CommentDetail.as_view())    
]
