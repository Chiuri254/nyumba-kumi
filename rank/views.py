from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.takes request from user processes it and returns it.
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