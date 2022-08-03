import imp
from django.urls import path
from location.views import index
urlpatterns = [
    path('',index)
]
