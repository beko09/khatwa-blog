from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404,Http404
from django.contrib import messages
from django.http import HttpResponse
from .forms import NewsletterForm,NewsCreationForm
from django.conf import settings
from .models import Info,NewsLetterUser
from django.core.mail import send_mail, get_connection,BadHeaderError,EmailMultiAlternatives
from django.template.loader import get_template
from posts.models import Category











def newsletter_singup(request):
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        #Here I am sure that the email is registered or not
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            #if email register show  messages warning
            messages.warning(request,f'هذا الايميل مشترك مسبقا')
        else:
            # if email not register save this email and show messages success
            instance.save()
            messages.success(request,f'تم الاشتراك بنجاح ')
            #l am use function send() to send email
            subject = " الاشتراك البريدي"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            #Here you can use an external text file so that you type what you want
            # with open(settings.BASE_DIR + "/templates/sign_up_email.txt") as f:
            #     signup_message = f.read()
            # lam use simle text
            signup_message = """ helo wel come """
            message = EmailMultiAlternatives(subject=subject,body=signup_message,from_email=from_email,to=to_email)
            html_template = get_template("about/sign_up_email.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()
    return {
        'form_subscrip': form
    }   
    # context ={
    #     'form': form
    # }   
    # return render(request,'base.html', context)


def category_list(request):
    categoryes = Category.objects.all()
    
    return  {
        'categoryes':categoryes
    }