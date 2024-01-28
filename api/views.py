from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .serilizer import *
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.db.models import Q, Sum
from .utils import send_to_email

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
        # check subscriber list and if blog is published then send email to all subscriber
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_blog(request, pk):
    blog = Blog.objects.filter(id == pk)
    blog = Blog_Seriliazers(blog, many=True)
    if blog:
        # update read column of review table
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
        # check subscriber list and if blog was not published and after edit it is pucblished now then send email to all subscriber
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    # delete all comments, review, image, other files, and reply of this blog
    blog.delete()
    return HttpResponse("Blog has been deleted sucessfully")

@api_view(['POST'])
def publish_blog(request, pk):
    Blog.objects.filter(id=pk).update(publish_blog=True)
    return HttpResponse("Blog has been sucessfully published")

@api_view(['POST'])
def share_blog(request):
    # share blog on email
    # update share column of review table
    send_to_email()
    return HttpResponse({"message": "Email has been send sucessfully"})

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
        # feedback email message to visitor and send an email to own for quick analysis
        return Response(const.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def comments(request):
    comment = Comments_Seriliazers(data=request.data)
    if comment.is_valid():
        comment.save()
        return Response(comment.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_comments(request):
    comments = Comments.objects.filter(Q(Comments.user_id == request.data.user_id) & Q(Comments.blog_id == request.data.blog_id)).all()
    comments = Comments_Seriliazers(comments, many=True)

    if comments:
        return Response(comments.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_comments(request, pk):
    comment = Comments.objects.filter(Q(Comments.user_id == request.data.user_id) & Q(Comments.blog_id == request.data.blog_id))
    comment = get_object_or_404(comment, id=pk)
    comment.delete()
    return HttpResponse("Comment has been deleted sucessfully")
    
@api_view(['POST'])
def review(request):
    blog_review = Review_Seriliazers(data=request.data)
    if blog_review.is_valid():
        blog_review.save()
        return Response(blog_review.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# coding logic might need to update
@api_view(['GET'])
def get_review(request):
    review = Review.objects.filter(Q(Review.blog_id == request.data.blog_id) & Q(Review.user_id == request.data.user_id)
        ).aggregate(like = Sum('like', default=0), dislike = Sum('dislike', default=0), share = Sum('share', default=0), read = Sum('read', default=0))
    review = Reply_Seriliazers(review, many=True)
    if review:
        return Response(review.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def reply(request):
    comment_reply = Reply_Seriliazers(data=request.data)
    if comment_reply.is_valid():
        comment_reply.save()
        return Response(comment_reply.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_reply(request):
    reply = Reply.objects.filter(
        Q(Reply.comment_id == request.data.comment_id)
        &Q(Reply.blog_id == request.data.blog_id)
        &Q(Reply.user_id == request.data.user_id)
    ).all()

    reply = Reply_Seriliazers(reply, many=True)
    if reply:
        return Response(reply.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_reply(request, pk):
    reply = Reply.objects.filter(
        Q(Reply.comment_id == request.data.comment_id)&
        Q(Reply.blog_id == request.data.blog_id)&
        Q(Reply.user_id == request.data.user_id)
    )
    reply = get_object_or_404(reply, id=pk)
    reply.delete()
    return HttpResponse("Comment has been sucessfully deleted")

@api_view(['GET'])
def search_blog(request, name):
    blog = Blog.objects.filter(
        Q(Blog.title__icontains == name)
        |Q(Blog.description__icontains == name)
        |Q(Blog.category__icontains == name)
    ).all()

    blog = Blog_Seriliazers(blog, many=True)
    if blog:
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

