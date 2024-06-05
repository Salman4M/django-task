from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import *


def owner_detail_view(request,id):
    owner=get_object_or_404(Owner,id=id)

    return render(request,'own_detail.html',{"owner":owner})


def gallery_view(request,id):
    gallery=get_object_or_404(Gallery,id=id)
    cars=Car.objects.filter(gallery=gallery)

    context={'gallery':gallery,'cars':cars}

    return render(request,'gall_det.html',context)




