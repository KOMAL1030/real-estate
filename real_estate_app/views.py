from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, state_choices, price_choices

# Create your views here.
from django.http import HttpResponse
 
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published =True) [:3]
    context= {
        'listings':listings,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices
    }
    return render(request, 'real_estate_app/index.html',context)

def about(request):
    realtors = Realtor.objects.all()
    mvp = Realtor.objects.all().filter(is_mvp = True)
    context= {
        'realtors': realtors,
        'mvp':mvp

    }
    return render(request, 'real_estate_app/about.html', context)

