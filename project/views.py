from django.shortcuts import render, redirect
from project.models import Project
from django.contrib.auth.decorators import login_required
from project.forms import CreateProject, ReviewForm
from django.contrib import messages

from project.utils import searchProjects, paginateProjects


def projects(request):
    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 6)

    context = {'projects': projects, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, "projects.html", context)


def tagsProjects(request, pk):
    projects, search_query = searchProjects(request)

    context = {'projects': projects, 'search_query': search_query}
    return render(request, "projects.html", context)



def project(request, projectId):
    # try:
    projectObj = Project.objects.get(id=projectId)
    tags = projectObj.tags.all()
    form = ReviewForm()
    context = {
        'project': projectObj,
        'tags': tags,
        'form': form
    }

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user.profile
            review.project = projectObj
            review.save()
            projectObj.getVoteCount 
            messages.success(request, "your review had been added Successfully")
            return redirect('project',projectId)
    return render(request, "project.html", context)


# except:
#     return render(request, "notFound.html")


@login_required(login_url="login")
def createProject(request):
    form = CreateProject()
    if request.method == "POST":
        data = CreateProject(request.POST, request.FILES)

        # profile = Profile.objects.get(user=request.user)

        profile = request.user.profile
        if data.is_valid():
            projectObj = data.save(commit=False)
            projectObj.owner = profile
            projectObj.save()
            messages.success(request, "project created")
            # if (request.POST.next)
            return redirect('my-account')
    context = {'form': form}
    return render(request, "createProject.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = CreateProject(instance=project)
    context = {'form': form}
    if request.method == "POST":
        if (request.user.profile != project.owner):
            messages.error(request, "cannot update others project")
            return render(request, "createProject.html", context)
        data = CreateProject(request.POST, request.FILES, instance=project)
        if data.is_valid():
            data.save()
            messages.success(request, "project updated")
            return redirect("my-account")

    return render(request, "createProject.html", context)


@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object': project}
    if request.method == "POST":
        if (request.user.profile != project.owner):
            messages.error(request, "cannot delete others project")
            return redirect('projects')
        project.delete()
        messages.success(request, "project deleted")
        return redirect("my-account")
    return render(request, 'delete.html', context)


def NotFound(request):
    return render(request, "notFound.html")
