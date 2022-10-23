from ast import keyword
from distutils.log import error
from urllib import response
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, Http404
from django.template import loader
from amadeus import Client, ResponseError, Location
from django.http import JsonResponse
from .models import Post
from apps import flight
# user Interface consuming the API within the Django Framework

def index(request):
    context = {'username': 'joelwembo'}
    return render(request, 'flight/index.html', context)


amadeus = Client(client_id='3HcWAkvN1fp6wxe3o5fXWAiMGedUzCxV', client_secret='2N4SnYPn4gDt9BP3')

def select_destination(req, param):
    if req.method == "GET":
        try:
            print(param)
            response = amadeus.reference_data.locations.get(keyword=param, subType=Location.ANY)
            context = {
                "data" : response.data
            }
            return JsonResponse(context)
        except ResponseError as error:
            print(error)
    else:
        return JsonResponse({"error": "Invalid request method"})   
    
    
def search_offers(req):
    if req.method == "GET":
        try:
            origin_code = req.GET["originCode"]
            destination_code = req.GET["destinationCode"]
            departure_date = req.GET["departureDate"]
            response = amadeus.shopping.flight_offers.search.get(  
                  originLocationCode=origin_code, 
                  destinationLocationCode=destination_code,
                  departureDate=departure_date, adults=2                                              
                                                                  
                        )
            
            context = {
                "data" : response.data
            }
            return JsonResponse(context)
        except ResponseError as error:
            print (error)
            
    else:
        return JsonResponse({"error": "Invalid request method"})        
                
    
    
    
def price_offer(req):
    if req.method == "GET":
        try:
            flight = req.POST['flight']
            response = amadeus.shopping.flight_offers.pricing.post(flight)
            print(response.data)
            return JsonResponse(response.data)
  
        except ResponseError as error:
            print(error)
            
    else:
        return JsonResponse({"error": "Invalid request method"})  
    
def book_flight(req):
    if req.method == "POST":
        try:
            flight = req.POST['flight']
            traveler = req.POST['traveler']
            booking = amadeus.booking.flight_orders.post(flight, traveler)
            return JsonResponse(booking)
        except ResponseError as error:
            print(error)
            
    else:
        return JsonResponse({"error": "Invalid request method"})        
        
       
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'flight/blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'flight/post_detail.html'