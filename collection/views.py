from django.shortcuts import render
# from build.pip.pip._vendor.requests.api import request

# Create your views here.
def index(request):
    return render(request, 'index.html')