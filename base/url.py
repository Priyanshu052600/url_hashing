from django.urls import path
from base.views import createurl, routetourl

urlpatterns = [
    path('',createurl),
    path('<slug:key>/',routetourl)
]
