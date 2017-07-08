from django.shortcuts import render
from collection.models import Pokemon
# from build.pip.pip._vendor.requests.api import request

# Create your views here.
def index(request):
    return render(request, 'index.html')

def MyView(request):
    query_results = Pokemon.objects.all()