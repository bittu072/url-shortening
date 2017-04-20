from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import ShortenURL

# Create your views here.
# function base view
def goshort_redirect_view(request, shorturl=None, *args, **kwargs):
    # obj = ShortenURL.objects.get(shorturl=shorturl)
    obj_url = "NONE"
    qs = ShortenURL.objects.filter(shorturl__iexact=shorturl.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url

    # OR
    # try:
    #     obj = ShortenURL.objects.get(shorturl=shorturl)
    # except:
    #     obj = ShortenURL.objects.all().first(

    return HttpResponse("hello..." + obj_url)


# class base view
# class goshortCBview(View):
#     def get(self, request, shorturl=None, *args, **kwargs):
#         # now after addding shorturl=None, arg and kwargs will be stored in shorturl
#         # this will also help to avoid the error
#         return HttpResponse("hello again!!" + shorturl)
#         # here shorturlcode will be whatever is after a/ in url address bar
#         # suppose url is entered "localhost:8000/a/xyz" then
#         # shorturlcode will be "xyz"
#         # check urls.py to see how we get shorturl
