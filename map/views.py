from django.shortcuts import render

from map.models import Tourism

# Create your views here.
def map(request):
    return render(request, 'map.html')