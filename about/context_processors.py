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
    """
    1- In this function the user will log in and send him 
    a thank you messageing this function user register 
    and send email
    
    2- check that the email is registered or not

    3- if email register show  messages warning

    4- if email not register save this email and
     show messages success

    5- and use function send() to send email

    6- last  you can use an external text 
    file so that you type what you want
    
    """
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            messages.warning(request,f'هذا الايميل مشترك مسبقا')
        else:
            instance.save()
            messages.success(request,f'تم الاشتراك بنجاح ')
            subject = " الاشتراك البريدي"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
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



def category_list(request):
    categoryes = Category.objects.all()
    
    return  {
        'categoryes':categoryes
    }