from django.shortcuts import render
from .models import mypost

# Create your views here.
def post_list(request):
    data = mypost.objects.all()
    return render(request,'post/index.html',{'post':data})
