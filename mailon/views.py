# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render 
from django.core.mail import send_mail
from emailman.settings import EMAIL_HOST_USER

def index_view(request):
    return render(request, "index.html")

def test(request):
    if request.method == "POST":
        subject = request.POST['subject']
        from_email = request.POST['to_email']
        message = request.POST['message']
        message = "Mail from  " + from_email + " : \n\n" + message
        context = {'from_email': from_email,}
        send_mail(subject, message,from_email, ['parthpandyappp@gmail.com'],)
        return render(request, "success.html", context)

    else:
        return render(request, "success.html")
# Create your views here.
