from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from APIs import views


urlpatterns = [
    path("", views.getRoutes, name="get-routes"),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/', views.projects, name="projects-api"),
    path('projects/<str:projectId>/', views.project, name="project-api"),
    path('users/', views.users, name="users-api"),
    path("projects/<str:pk>/vote/",views.voteProject),
    path('create-tag/',views.createTag)

]
