from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import states_choices, bedrooms_choices, prices_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings' : listings,
        'states_choices' : states_choices,
        'bedrooms_choices' : bedrooms_choices,
        'prices_choices' : prices_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors' : realtors,
        'mvp_relators' : mvp_realtors
    }
    return render(request, 'pages/about.html', context)

