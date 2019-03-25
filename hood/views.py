from django.shortcuts import render,redirect
from .models import Image,Category,Location,Health,Authorities,Profile
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def welcome(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'welcome.html')

def display_location(request,location_id):
    try:
        locations = Location.objects.all()
        location = Location.objects.get(id = location_id)
        images = Image.objects.filter(image_location = location.id)
    except:
        raise Http404()
    return render(request,'location.html',{'location':location,'images':images,'locations':locations})

def search_category(request):
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = (request.GET.get('category')).title()
        searched_images = Image.search_by_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{'message':message,'images':searched_images,'locations':locations})

    else:
        message = "You haven't searched for any category"
        return render(request,'search.html',{'message':message,'locations':locations})

# @login_required(login_url='/accounts/login/')
def health(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood)

   
    return render(request,'health.html',{"healthservices":healthservices})
    
# @login_required(login_url='/accounts/login/')
def authorities(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    authorities = Authorities.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'authorities.html',{"authorities":authorities})