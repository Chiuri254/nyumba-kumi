from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  MoringaMerch
from .serializer import MerchSerializer
from .models import Profile, Project, Review


# Create your views here.takes request from user processes it and returns it.
# @login_required(login_url='/accounts/login/')
def welcome(request):
    if User.objects.filter(username = request.user.username).exists():
        user = User.objects.get(username=request.user)
        if not Profile.objects.filter(user = request.user).exists():
            Profile.objects.create(user = user)   
    projects = Project.objects.order_by('-pub_date')
    return render(request,"welcome.html",{"projects":projects})



class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)