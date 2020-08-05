from django.shortcuts import render,get_object_or_404
from .models import Info




def about(request):
    about_us = get_object_or_404(Info)

    context = {
        'about_us':about_us
    }
    return render(request,"about/about-us.html", context)

