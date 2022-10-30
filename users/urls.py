from django.urls import path

from users import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.loginForm, name="login"),
    path("logout/", views.logoutForm, name="logout"),
    path("", views.users, name="users"),
    path("user/<str:userId>", views.user, name="user-profile"),
    path("update-user-profile/", views.updateUserProfile,
         name="update-user-profile"),
    path("account/", views.account, name="my-account"),
    path("add-skill/", views.createSkill, name="add-skill"),
    path("update-skill/<str:pk>/", views.updateSkill, name="update-skill"),
    path("delete-skill/<str:pk>/", views.deleteSkill, name="delete-skill"),
    path('send-message/<str:pk>/', views.sendMessage, name="send-message"),
    path('messages/', views.userInbox, name="user-inbox"),
]
