from django.shortcuts import render

from django.views.generic import ListView , DetailView , CreateView
from .models import Property



class PropertyList(ListView):
    model = property 
    #filter



class PropertyDetail(DetailView):
    pass
    #book


