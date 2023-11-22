from django.urls import path, include
from league import views

urlpatterns = [
    path('epl-table/', views.SeasonList.as_view()),
    path('epl-table/<int:pk>', views.SeasonDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('authenticate-api/', include("rest_framework.urls")),
]