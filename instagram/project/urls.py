from django.urls import path

from project import views

urlpatterns = [
    path("projects/", views.projects, name="projects"),
    path("project/<str:projectId>", views.project, name="project"),
    path("create-project/", views.createProject, name="create-project"),
    path("update-project/<str:pk>", views.updateProject, name="update-project"),
    path("delete-project/<str:pk>", views.deleteProject, name="delete-project"),
]
 