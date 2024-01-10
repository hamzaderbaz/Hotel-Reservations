from django.shortcuts import redirect, render

from django.views.generic import ListView , DetailView , CreateView
from django.views.generic.edit import FormMixin
from .models import Property , PropertyImages , PropertyReview , Category
from .forms import PropertyBookForm
from django.urls import reverse
from django.contrib import messages
from .filters import PropertyFilter
from django_filters.views import FilterView

from django.db.models import Avg


class PropertyList(FilterView):
    model = Property
    paginate_by = 3
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        properties = context['object_list']
        reviews = {}

        for property in properties:
            property_reviews = PropertyReview.objects.filter(property=property)
            avg_rating = property_reviews.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
            num_of_stars = int(avg_rating)  # Ensure the number of stars is an integer
            reviews[property.id] = {'avg_rating': avg_rating, 'num_of_stars': range(num_of_stars)}
        
        context['property_reviews'] = reviews
        return context



class PropertyDetail(FormMixin , DetailView):
    model = Property
    form_class = PropertyBookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["property_images"] = PropertyImages.objects.filter(property=self.get_object().id)
        context['get_related'] = Property.objects.filter(category=self.get_object().category)[:3]
        # context['review_count'] = PropertyReview.objects.filter(property=self.get_object()).count()

        return context


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()
            messages.success(request, 'Your Reservation Confirmed ')
            return redirect(reverse('property:property_detail' , kwargs={'slug':self.get_object().slug}))