from django.shortcuts import redirect, render
from project.models import Project
from project.forms import CreateProject


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {'projects': projects})


def project(request, projectId):
    projectObj = Project.objects.get(id=projectId)
    tags = projectObj.tags.all()
    return render(request, "project.html", {'project': projectObj, 'tags': tags})


def createProject(request):
    form = CreateProject()
    print(request)
    if request.method == "POST":
        data = CreateProject(request.POST)
        if data.is_valid():
            data.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "createProject.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = CreateProject(instance=project)

    if request.method == "POST":
        data = CreateProject(request.POST, instance=project)
        if data.is_valid():
            data.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "createProject.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    # form = CreateProject(instance=project)

    # if request.method == "POST":
    # data = CreateProject(request.POST)
    # print(data)
    # if data.is_valid():
    # data.save()
    print(project)
    project.delete()
    return redirect('projects')
    # context = {'form': 'form'}
    # return render(request, "createProject.html", context)
