from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
# function base view
def goshort_redirect_view(request, shorturl=None, *args, **kwargs):
    # now after addding shorturl=None, arg and kwargs will be stored in shorturl
    # this will also help to avoid the error
    return HttpResponse("hello..." + shorturl)
    # here shorturlcode will be whatever is after a/ in url address bar
    # suppose url is entered "localhost:8000/a/xyz" then
    # shorturlcode will be "xyz"
    # check urls.py to see how we get shorturl

# class base view
class goshortCBview(View):
    def get(self, request, shorturl=None, *args, **kwargs):
        return HttpResponse("hello again!!" + shorturl)
