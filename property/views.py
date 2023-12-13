from django.shortcuts import render

from django.views.generic import ListView , DetailView 
from .models import Property



class PropertyList(ListView):
    # pass
    model = Property 
    #filter



class PropertyDetail(DetailView):
    pass
    #book


