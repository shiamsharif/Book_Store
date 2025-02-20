from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import ContactForm
import os

def Send_mail(self, form):
        contact = form.save()

        # Email details
        subject = f"New Contact Form Submission from {contact.name}"
        message = f"""
        Name: {contact.name}
        Email: {contact.email}
        
        Message:
        {contact.message}
        """
        sender_email = os.getenv("EMAIL_HOST_USER")  # Get from .env
        recipient_email = ["shiamsharif.dev@gmail.com","shiamsharif.07@gmail.com"]  # Your email

        # Send email
        send_mail(subject, message, sender_email, recipient_email)