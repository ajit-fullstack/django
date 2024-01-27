from .models import *
from rest_framework.serializers import ModelSerializer

class Blog_Seriliazers(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class Review_Seriliazers(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class Comments_Seriliazers(ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class Reply_Seriliazers(ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"

class Subscribe_Seriliazers(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"

class Contact_Seriliazers(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
