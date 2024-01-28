from django.db.models import Model, CharField, IntegerField, DateTimeField, TextField, BooleanField, CASCADE

# Create your models here.
class OTP(Model):
    email_id= CharField(max_length=50, default=None)
    otp= IntegerField()
    created = DateTimeField(auto_now=True)

class Blog(Model):
    title = CharField(max_length=500, default=None)
    description = TextField()
    category = CharField(max_length=80, default=None)
    publish_blog = BooleanField(default=False)
    keywords = TextField() 
    created = DateTimeField(auto_now=True)
    updated = DateTimeField(auto_now_add=True)
    user_id = IntegerField() 

class Review(Model):
    like = IntegerField()
    dislike = IntegerField()
    share = IntegerField()
    read = IntegerField()
    blog_id = IntegerField()  # Froegin key
    user_id = IntegerField()  # Froegin key

class Comments(Model):
    message = TextField()
    created = DateTimeField(auto_now=True)
    blog_id = IntegerField()  # Froegin key
    user_id = IntegerField()  # Froegin key
    

class Reply(Model):
    message = TextField()
    created = DateTimeField(auto_now=True)
    comment_id = IntegerField()  # Froegin key
    blog_id = IntegerField()  # Froegin key
    user_id = IntegerField()  # Froegin key
    

class Subscribe(Model):
    email_id = CharField(max_length=80, default=None)
    created = DateTimeField(auto_now=True)
    

class Contact(Model):
    userName = CharField(max_length=50, default=None)
    email_id = CharField(max_length=80, default=None)
    mobile = IntegerField()
    subject = CharField(max_length=100, default=None)
    message = TextField()
    created = DateTimeField(auto_now=True)

