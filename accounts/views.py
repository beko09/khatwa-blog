from django.shortcuts import (
    render, reverse,
    redirect, get_object_or_404,
    HttpResponseRedirect
    )
from .forms import (
    RegisterForm, UserForm,
    ProfileForm
     )
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib.auth.models import User
from posts.models import Post  
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from project.tokens import account_activation_token
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'تفعيل حساب المدونة الخاص بك.'
            current_site = get_current_site(request)
            mail_subject = 'تفعيل حساب المدونة الخاص بك.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),#.decode()
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, f' تم ارسال رسالة الي ايميلك لاكمال عملية التسجيل يرجي مراجعة الايميل!')
            return redirect('/')
            # form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # # return redirect('/')
            # return HttpResponseRedirect(reverse('accounts:profile', args=(username,)))
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
            return HttpResponseRedirect(reverse('accounts:profile', args=(username,)))

    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)

    context = {
        'userForm': userForm,
        'profileForm': profileForm
    }
    return render(request, 'registration/profile_edit.html', context)




def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, f'شكرا لتأكيد بريدك الالكتروني الآن اكتمل تسجيل  حسابك')
        login(request, user)
        return redirect('/')
       
        # return redirect('login')
    else:
        return HttpResponse('رابط التنشيط غير صالح')