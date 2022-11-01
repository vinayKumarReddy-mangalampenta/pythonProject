from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from APIs.serializers import ProjectSerializer, ProfileSerializer
from project.models import Project, Tag
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


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def voteProject(request, pk):
    projectObj = Project.objects.get(id=pk)

    review, created = projectObj.review_set.get_or_create(
        owner=request.user.profile)
    review.value = request.data.get('vote')
    review.save() 
    projectObj.getVoteCount

    return Response({'result': "you have {vote}voted the {project} project successfully".format(vote=request.data.get('vote'), project=projectObj)})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTag(request):
    tagObj = Tag.objects.create(name=request.data.get('tagName'))
    tagObj.save()
    return Response({'result': "{tagObj} created successfully".format(tagObj=tagObj)})

