from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    # url('today$',views.rank_of_the_day,name='newsToday'),
    # url(r'^search/', views.search_results, name='search_results')
    #  url(r'^api/merch/$', views.MerchList.as_view()),
]