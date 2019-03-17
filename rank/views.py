from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  MoringaMerch
from .serializer import MerchSerializer


# Create your views here.takes request from user processes it and returns it.
# @login_required(login_url='/accounts/login/')
def welcome(request):
      return render(request, 'welcome.html')

def rank_of_the_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
                </body>
                </html>
                '''
    return HttpResponse(html)

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)