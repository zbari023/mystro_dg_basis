from django.shortcuts import render
from .models import mypost

# Create your views here.
def post_list(request):
    data = mypost.objects.all()
    return render(request,'post/index.html',{'post':data})

def post_details(request,post_id):
    data = mypost.objects.get(id=post_id)
    return render(request,'post/iddetails.html',{'post':data})