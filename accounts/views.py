from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Profile
from .forms import UserForm , ProfileForm , UserCreateForm
from django.contrib import messages
from property.models import PropertyBook , Property
from property.forms import PropertyReviewForm




def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})



def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile') 
            else:
                error_message = "Invalid username or password."
                return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})



def profile(request):
    profile = Profile.objects.get(user=request.user)
    user_reservation = Property.objects.filter(owner=request.user)
    return render(request, 'profile/profile.html', {'profile': profile, 'user_reservation': user_reservation})



def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST , request.FILES , instance=profile)
    
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect(reverse('accounts:profile'))
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance = profile)       

    return render(request,'profile/profile_edit.html',{
        'user_form' : user_form , 
        'profile_form' : profile_form
    })

def logout(request):
    auth_logout(request)
    return render(request, 'registration/logged_out.html') 



def my_reservation(request):
    user_reservation = PropertyBook.objects.filter(user=request.user)
    return render(request,'profile/my_reservation.html' , {'user_reservation':user_reservation})

def my_listing(request):
    user_reservation = Property.objects.filter(owner=request.user)
    return render(request,'profile/my_listing.html' , {'user_reservation':user_reservation})


def delete_property(request, property_id):
    property_to_delete = get_object_or_404(Property, pk=property_id)

    if request.method == 'POST':
        # Soft delete logic
        property_to_delete.is_deleted = True
        property_to_delete.save()
        return redirect('accounts:my_listing')  # Redirect to your property list view

    return render(request, 'delete_property_confirm.html', {'property': property_to_delete})







def add_feedback(request , slug):
    property = get_object_or_404(Property , slug=slug)
    if request.method == 'POST':
        form = PropertyReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = property
            myform.author = request.user
            myform.save()

    else:
        form = PropertyReviewForm()

    return render(request,'profile/property_feedback.html' , {'form':form , 'property':property})



