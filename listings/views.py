from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing
from .choices import states_choices, bedrooms_choices, prices_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'listings' : page_obj
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing' : listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    query_result = Listing.objects.order_by('-list_date')

    #keyword filter
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_result = query_result.filter(description__icontains=keywords)

    #city filter
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_result = query_result.filter(city__iexact=city)

    
    #keyword filter
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_result = query_result.filter(state__iexact=state)

    #keyword filter
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_result = query_result.filter(bedrooms__lte=bedrooms)

    #keyword filter
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_result = query_result.filter(price__lte=price)



    context = {
        'listings' : query_result,
        'states_choices' : states_choices,
        'bedrooms_choices' : bedrooms_choices,
        'prices_choices' : prices_choices,
        'values' : request.GET
    }
    
    return render(request, 'listings/search.html', context)

