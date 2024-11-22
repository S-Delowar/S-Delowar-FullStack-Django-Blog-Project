from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    # return HttpResponse("Home Page active now")
    return render(request, "pages/home.html")