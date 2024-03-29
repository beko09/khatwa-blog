from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404,Http404
from django.contrib import messages
from .models import NewsLetterUser
from django.http import HttpResponse
from .forms import NewsletterForm,NewsCreationForm
from django.conf import settings
from .models import Info
from django.core.mail import send_mail, get_connection,BadHeaderError,EmailMultiAlternatives
from django.template.loader import get_template




def about(request):
    about_us = Info.objects.all()
    context = {
        'abouts':about_us,
    }
    return render(request, "about/about.html", context)


def newsletter_unsubscribe(request):
    """
     1- In this function I cancel the subscription. 

     2- I first verify that the email entered by the 
     user is in a table NewsLetterUser.

    3- and  Sending a farewell message.
    if email in table then delete this email

    4- already cleared from the table and then
     I send a farewell message.

    5- Here I bring the email form and not from the 
    table because the email was

    """
    email = request.GET.get("email")
    if email:
        if NewsLetterUser.objects.filter(email=email).exists():
            subject = "شكرا لك"
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            signup_message = """ helo wel come """
            message = EmailMultiAlternatives(subject=subject,body=signup_message,from_email=from_email,to=to_email)
            html_template = get_template("about/unsub_email.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()
            email_un = NewsLetterUser.objects.filter(email=email)
            email_un.delete()
            if request:
                messages.success(request, f'تم الغاء الاشتراك  ')
            return redirect("/")
        else:
            messages.warning(request,f'هذا الايميل غير موجود ')
       
    return render(request,'about/newsletter_unsubscribe.html', {})



def control_newsletter(request):
    """
    1- In this function I send new news to those 
     who have registered in the mailing list

    2-  I bring the amyla from a table NewsLetterUser 
     I only take the values of the field

    3- And then convert the values  to list to
      ease send with function send_email
    """
    getemail = NewsLetterUser.objects.all().values_list('email',flat=True).distinct()
    email2=list(getemail)
    if request.method == 'POST':
        form = NewsCreationForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data['message']
            email = email2
            try:
                send_mail(subject, message, from_email,email,fail_silently=True)
            except BadHeaderError:
                messages.warning(request,f'هذا الايميل غير موجود ')
                return redirect("/control_newsletter")
            messages.success(request,f'تم ارسال الايميل بنجاح لجميع المشتركين')
            return redirect("/")
    else:
        form = NewsCreationForm()       
    
    return render(request, 'about/control_newsletter.html', {'forms': form})


