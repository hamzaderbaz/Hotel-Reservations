from django import forms
from .models import Property, PropertyBook , PropertyReview


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'image', 'price','description','place','category']
        # fields = '__all__'

class PropertyBookForm(forms.ModelForm):
    date_from = forms.DateField(widget= forms.DateInput(attrs={'id':'checkin_date'}))
    date_to = forms.DateField(widget= forms.DateInput(attrs={'id':'checkin_date'}))
    class Meta:
        model = PropertyBook

        # fields = '__all__'
        fields = ['date_from', 'date_to', 'guest', 'children']




class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = PropertyReview
        fields = ['rating','feedback']


