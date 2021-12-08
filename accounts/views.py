from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contacts

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if(user is not None):
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Password Validation
        if(password == password2):
            #User Name Validation
            if(User.objects.filter(username=username).exists()):
                messages.error(request, 'username already exists.')
            else:
                #Email Validation
                if(User.objects.filter(email=email).exists()):
                    messages.error(request, 'email already exists.')
                else:
                    #All Validation Passed 
                    user = User.objects.create_user(first_name=first_name, last_name=last_name,
                    username=username, email=email, password=password)
                    user.save()
                    messages.success(request, username +' registered Successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'password does not match')
            return redirect('register')
        
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are Now logged out.')
        return redirect('index')
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated :
        user_contacts = Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)
        context = {
            'contacts' : user_contacts 
        }
        return render(request, 'accounts/dashboard.html', context)
    messages.error(request, 'user is not authenticated.')
    return redirect('login')



