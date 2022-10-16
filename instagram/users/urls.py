from django.urls import path

from users import views

urlpatterns = [
    path("", views.users, name="users"),
    path("user/<str:userId>", views.user, name="user"),
    path("create-user-profile/", views.createUserProfile, name="create-user"),
]
