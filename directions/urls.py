from django.urls import path, include
from directions import views

urlpatterns = [
    path('directions/', views.DirectionList.as_view()),
    path('directions/<int:pk>/', views.DirectionDetail.as_view()),
]