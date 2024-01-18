from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.mail import send_mail

from .models import Info
from django.conf import settings

# def contact(request):
#     return render(request, 'contact/contact.html')


def send_message(request):
    myinfo = Info.objects.first()
    
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        email = EmailMessage(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  # Set your sending email here
            [settings.DEFAULT_FROM_EMAIL],  # Your email address where you want to receive these messages
            reply_to = [user_email],  # Set the reply-to field to the user's email
        )

        email.from_email = f'{user_name} <{user_email}>'  # Set sender's display name and email
        email.send()
        messages.success(request, 'Your Email Was Sent Successfully!')
        return redirect('contact:contact')
    
    return render(request, 'contact/contact.html', {'myinfo': myinfo})



# def contact(request):
#     site_info = Info.objects.last()

#     if request.method == 'POST':
#         subject = request.POST['subject']
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']


#         send_mail_task.delay(subject , name,email,message)


#     return render(request,'settings/contact.html',{'site_info': site_info})