from django.shortcuts import render
from .models import *
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_desc=data.get('receipe_desc')
        receipe_image=request.FILES.get('receipe_image')
        Receipe.objects.create(
            receipe_name=receipe_name,
             receipe_desc= receipe_desc,
              receipe_image= receipe_image
         )
    return render(request,'receipes.html')
# Create your views here.
       