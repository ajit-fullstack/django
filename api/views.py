from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serilizer import *
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

# Create your views here.
@api_view(["POST"])
def user_login(request):
    pass

@api_view(["POST"])
def user_regestration(request):
    pass

@api_view(["POST"])
def forgot_pass(request):
    pass

@api_view(['POST'])
def verify_otp(request):
    pass

@api_view(['POST'])    
def change_pass(request):
    pass




@api_view(['POST'])
def create_blog(request):
    blog = Blog_Seriliazers(data=request.data)
    if blog.is_valid():
        blog.save()
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_blog(request, pk):
    blog = Blog.objects.filter(id == pk)
    blog = Blog_Seriliazers(blog, many=True)
    if blog:
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_all_blog(request):
    blogs = Blog.objects.all()
    blogs = Blog_Seriliazers(blogs, many=True)
    if blogs:
        return Response(blogs.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_blog_cat(request, cat):
    blog = Blog.objects.filter(category= cat).all()
    blog = Blog_Seriliazers(blog, many=True)
    if blog:
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_blog(request, pk):
    blog = Blog.objects.filter(id=pk)
    blog = Blog_Seriliazers(instance=blog, data=request.data)
    if blog.is_valid():
        blog.save()
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return HttpResponse("Blog has been deleted sucessfully")

@api_view(['POST'])
def publish_blog(request, pk):
    Blog.objects.filter(id=pk).update(publish_blog=True)
    return HttpResponse("Blog has been sucessfully published")

@api_view(['POST'])
def share_blog(request, pk):
    pass

@api_view(['POST'])
def subscribe(request):
    data = Subscribe_Seriliazers(data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def unsubscribe(request):
    check = Subscribe.objects.filter(Subscribe.email_id==request.data.email_id)
    if check:
        check.delete()
        return HttpResponse("You have sucessfully unsubscribe our daily updates")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def contact(request):
    const = Contact_Seriliazers(data=request.data)
    if const.is_valid():
        const.save()
        return Response(const.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def comments(request):
    pass

@api_view(['GET'])
def get_comments(request):
    pass

@api_view(['DELETE'])
def delete_comments(request, pk):
    pass

@api_view(['POST'])
def review(request):
    pass

@api_view(['GET'])
def get_review(request):
    pass

@api_view(['POST'])
def reply(request):
    pass

@api_view(['GET'])
def get_reply(request):
    pass

@api_view(['DELETE'])
def delete_reply(request, pk):
    pass

@api_view(['GET'])
def search_blog(request, name):
    pass

