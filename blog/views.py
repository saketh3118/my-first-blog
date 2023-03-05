from django.shortcuts import render
from blog.models import Blog 
from django.utils import timezone
# Create your views here.
def post_list(request):
    post=Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'post_list.html',{'posts':post})