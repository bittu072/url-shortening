from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function base view
def goshort_redirect_view(request, *args, **kwargs):
    return HttpResponse("hello")

# class base view
class goshortCBview(view):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello again!!")
