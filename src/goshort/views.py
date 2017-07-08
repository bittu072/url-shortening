from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ShortenURL
from .forms import URLSubmit

# Create your views here.
# function base view
# def goshort_redirect_view(request, shorturl=None, *args, **kwargs):
#     obj = get_object_or_404(ShortenURL, shorturl=shorturl)
#     return HttpResponseRedirect("http://"+obj.url)

# class base view
class goshortCBview(View):
    def get(self, request, shorturl=None, *args, **kwargs):
        obj = get_object_or_404(ShortenURL, shorturl=shorturl)
        return HttpResponseRedirect("http://"+obj.url)

class GoShortView(View):
    def get(self, request, *args, **kwargs):
        the_form = URLSubmit()
        context = {
            "title": "Shorten the URL",
            "form": the_form
        }
        return render(request, "goshort/index.html", context)

    def post(self, request, *args, **kwargs):
        # print (request.POST)
        # print (request.POST.get("url"))
        form = URLSubmit(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        context = {
            "title": "Shorten the URL",
            "form": form
            }
        return render(request, "goshort/index.html", context)
