from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contacts

def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already contacted with this listing')
                return redirect('/listings/' + listing_id)


        contact = Contacts(listing=listing, listing_id=listing_id, name=name, email=email,
                phone=phone, message=message, user_id=user_id)
        contact.save()

        # send_mail(
        #     'Property Enquiry Email',
        #     'There has been enquiry request sent by user for ' + listing + '. Please check admin panel for more info.' ,
        #     'abhishekkumargswi@gmail.com',
        #     ['abhi9711182072@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'your request is submitted, the realtor will get back to you soon.')


        return redirect('/listings/' + listing_id)
