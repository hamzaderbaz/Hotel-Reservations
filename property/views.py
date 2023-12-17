from django.shortcuts import render

from django.views.generic import ListView , DetailView 
from .models import Property



class PropertyList(ListView):
    model = Property 
    #filter
    # pass



class PropertyDetail(DetailView):
    model = Property
    #book


