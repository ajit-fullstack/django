from django.shortcuts import render
from rest_framework.decorator import api_view

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
    pass

@api_view(['GET'])
def get_blog(request, pk):
    pass

@api_view(['GET'])
def get_all_blog(request):
    pass

@api_view(['GET'])
def get_blog_cat(request, cat):
    pass

@api_view(['PUT'])
def update_blog(request, pk):
    pass

@api_view(['DELETE'])
def delete_blog(request, pk):
    pass

@api_view(['POST'])
def publish_blog(request, pk):
    pass

@api_view(['POST'])
def publish_blog(request, pk):
    pass

@api_view(['POST'])
def share_blog(request, pk):
    pass

@api_view(['POST'])
def subscribe(request):
    pass

@api_view(['POST'])
def unsubscribe(request):
    pass

@api_view(['POST'])
def contact(request):
    pass

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

