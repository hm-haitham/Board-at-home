from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import RegistrationForm, UserProfileForm
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    numbers = [1,2,3,4,5]
    name = "Julius Pasion"
    args = {'myName': name,'numbers' : numbers }
    return render(request, "accounts/home.html", args)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)


        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            return redirect('/accounts')
    else:
        form = RegistrationForm()
        profile_form = UserProfileForm()

        args = {'form':form, 'profile_form': profile_form}
        return render(request,'accounts/reg_form.html', args)


def search(request):
    return render(request, "accounts/Search_Page.html")

def profile(request):
    args ={'user': request.user}
    return render(request, "accounts/profile.html", args)
