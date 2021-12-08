from django.shortcuts import render, redirect
from .models import Birthday
# Create your views here.

def birthday(request, name):
    print(name)
    birthdayuserdata = Birthday.objects.filter(name=name).first()
    print(birthdayuserdata)
    print(birthdayuserdata)
    context = {
        'data' : birthdayuserdata
    }
    print(name)
    if birthdayuserdata:
        return render(request, 'birthday/birthday.html', context)
    return redirect('listings')
    


