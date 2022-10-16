from django.shortcuts import render

from users.forms import CreateUserProfile


def users(request):
    return render(request, "users.html")


def user(request, userId):
    return render(request, "user.html", {"userId": userId})


def createUserProfile(request):
    form = CreateUserProfile()
    print(form)
    context = {'form': form}
    return render(request, "createUser.html", context)
