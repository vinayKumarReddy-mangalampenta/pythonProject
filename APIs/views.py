from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


from APIs.serializers import ProjectSerializer, ProfileSerializer
from project.models import Project
from users.models import Profile


def getRoutes(request):
    return HttpResponse("Hello world")


@api_view(['GET', 'POST'])
def projects(request):
    projectsObjs = Project.objects.all()
    serializer = ProjectSerializer(projectsObjs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def project(request, projectId):
    projectsObj = Project.objects.get(id=projectId)
    serializer = ProjectSerializer(projectsObj, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def users(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
