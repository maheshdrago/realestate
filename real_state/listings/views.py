from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import *


def index(request):


    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
    'listings': paged_listings,
    'state_choices':state_choices,
    'bedroom_choices':bedroom_choices,
    'price_choices':price_choices,
    'title':'Featured Listings'
  }
   
    return render(request,"listings/index.html",context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    
    context = {
        'listing':listing,
        'title':'Listing'
    }
    return render(request,"listings/listing.html",context)

def search(request):

    listings = Listing.objects.order_by('-list_date')


    #Keywords

    if 'keywords' in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            listings = listings.filter(description__icontains=keywords)


    #City

    if 'city' in request.GET:
        city = request.GET["city"]
        if city:
            listings = listings.filter(city__iexact=city)

    
    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state__iexact=state)
    
    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)
 
    context = {
    'values':request.GET,
    'listings':listings,
    'state_choices':state_choices,
    'bedroom_choices':bedroom_choices,
    'price_choices':price_choices,
    'title':'Listings'
  }
    return render(request,"listings/search.html",context)











'''
asgiref==3.3.1
astroid==2.4.2
autopep8==1.5.4
certifi==2020.12.5
colorama==0.4.3
Django==3.1.4
isort==5.5.3
lazy-object-proxy==1.4.3
mccabe==0.6.1
Pillow==8.0.1
psycopg2==2.8.6
pycodestyle==2.6.0
pylint==2.6.0
pytz==2020.5
six==1.15.0
sqlparse==0.4.1
toml==0.10.1
wincertstore==0.2
wrapt==1.12.1
'''