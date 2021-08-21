from django.shortcuts import render, redirect
import uuid
from .models import Shorter
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:6]
        new = Shorter(link = link, uuid = uid)
        new.save()
        return HttpResponse(uid)
    else:
        return HttpResponse(uid)

def go(request, pk):
    url_details =Shorter.objects.get(uuid = pk)
    return redirect('https://'+url_details.link)