from django.shortcuts import render, reverse, redirect
from .forms import RegisterForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
    

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile/')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)
    

def profile(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'profile': profile
    }

    return render(request, 'registration/profile.html', context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=request.user)
        profileForm = ProfileForm(
            request.POST, request.FILES, instance=profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            my_profile = profileForm.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)

    context = {
        'userForm': userForm,
        'profileForm': profileForm
    }
    return render(request, 'registration/profile_edit.html', context)
