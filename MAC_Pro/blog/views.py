from django.shortcuts import render
from django.http import HttpResponse
from .models import blogPost
# Create your views here.

def index(request):
    myposts = blogPost.objects.all()
    print(myposts)
    return render(request, 'blog_template/index.html', {'myposts': myposts})


def blogpost(request, id):
    post = blogPost.objects.filter(post_id=id)[0]
    return render(request, 'blog_template/blogpost.html', {'post':post})