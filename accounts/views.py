from django.shortcuts import render, reverse, redirect, get_object_or_404,HttpResponseRedirect
from .forms import RegisterForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth.models import User
from posts.models import Post  

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # return redirect('/')
            return HttpResponseRedirect(reverse('accounts:profile', args=(username,)))
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)
    

def profile(request, username):
    username = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=username)
    posts = Post.objects.filter(user=username)[:50]

    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'registration/profile.html', context)


def profile_edit(request,username):
    username = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=username)

    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=request.user)
        profileForm = ProfileForm(
            request.POST, request.FILES, instance=profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            my_profile = profileForm.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            # return redirect(reverse('accounts:profile'))
            return HttpResponseRedirect(reverse('accounts:profile', args=(username,)))

    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)

    context = {
        'userForm': userForm,
        'profileForm': profileForm
    }
    return render(request, 'registration/profile_edit.html', context)
