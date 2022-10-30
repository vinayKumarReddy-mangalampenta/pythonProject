from django.shortcuts import redirect, render

from users.forms import MessagesForm, UpdateUserProfile, CustomUserCreationForm, SkillForm
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.utils import searchProfiles, paginateProfiles




def users(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 6)

    context = {'profiles': profiles, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, "profiles.html", context)


def user(request, userId):
    profile = Profile.objects.get(id=userId)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    # projects = profile.project.all()

    return render(request, "profile.html", {"profile": profile, 'topSkills': topSkills, "otherSkills": otherSkills})

# created by you to add new fields check


@login_required(login_url='login')
def updateUserProfile(request):
    profile = request.user.profile
    form = UpdateUserProfile(instance=profile)
    if request.method == "POST":
        form = UpdateUserProfile(request.POST, request.FILES, instance=profile)
        form.save()
        return redirect("my-account")
    context = {'form': form}
    return render(request, "updateUserProfile.html", context)


def loginForm(request):
    context = {'page': 'login'}
    if request.user.is_authenticated:
        return redirect("projects")
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user not available")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
           

            messages.success(request, "logged in ")
            return redirect(request.GET['next'] if 'next' in request.GET else 'my-account')
        else:
            messages.error(request, "username or password wrong")

    return render(request, "login.html", context)


def logoutForm(request):
    logout(request)
    return redirect("login")


def register(request):
    form = CustomUserCreationForm()
    context = {'page': 'register', 'form': form}
    if request.method == 'POST':
        data = CustomUserCreationForm(request.POST)
        if data.is_valid():
            user = data.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "created account  successfully ")
            login(request, user)
            return redirect("projects")
        # else:
        #     messages.error(request, "please fill all fields correctly")

    return render(request, "login.html", context)


@login_required(login_url="login")
def account(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, "account.html", context)


@login_required(login_url="login")
def createSkill(request):
    form = SkillForm()
    context = {'form': form, 'page': 'create'}
    if request.method == "POST":
        form = SkillForm(request.POST)
        data = form.save(commit=False)
        data.owner = request.user.profile
        data.save()
        messages.success(request, "skill added")
        return redirect("my-account")
    return render(request, 'createSkill.html', context)


@login_required(login_url="login")
def updateSkill(request, pk):
    skill = request.user.profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    context = {'form': form, 'page': 'update'}
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        form.save()
        messages.success(request, "skill updated")
        return redirect("my-account")
    return render(request, 'createSkill.html', context)


@login_required(login_url="login")
def deleteSkill(request, pk):
    skill = request.user.profile.skill_set.get(id=pk)

    context = {'object': skill}
    if request.method == "POST":
        skill.delete()
        messages.success(request, "skill deleted")
        return redirect("my-account")
    return render(request, 'delete.html', context)

@login_required(login_url="login")
def sendMessage(request,pk):
    form = MessagesForm()
    context = {'form':form,'data':request.META}

    if request.method == "POST":
        form = MessagesForm(request.POST)
        obj = form.save(commit=False)
        obj.sender  = request.user.profile 
        obj.receiver = Profile.objects.filter(id=pk)[0]
        obj.save()
        messages.success(request,'message sent successfully')
        
        return redirect('profiles')


    return render(request,"createMessage.html",context)

@login_required(login_url="login")
def userInbox(request):
    # messagesList = request.user.profile.message_set.all()
    context = {
        
    }
    return render(request,"messages.html",context)