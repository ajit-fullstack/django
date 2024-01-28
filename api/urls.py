from django.urls import path
from .views import *

urlpatterns = [
    path("login/", user_login, name="login"),
    path("register/", user_regestration, name="register"),
    path("forgot_pass/", forgot_pass, name="forgot_pass"),
    path("verify_otp/", verify_otp, name="verify_otp"),
    path("change_pass/", change_pass, name="change_pass"),
    path("create_blog/", create_blog, name="create_blog"),
    path("get_blog/<int:pk>/", get_blog, name="get_blog"),
    path("get_all_blog", get_all_blog, name="get_all_blog"),
    path("get_blog_cat/<str:cat>/", get_blog_cat, name="get_blog_cat"),
    path("update_blog/<int:pk>/", update_blog, name="update_blog"),
    path("delete_blog/<int:pk>/", delete_blog, name="delete_blog"),
    path("publish_blog/<int:pk>/", publish_blog, name="publish_blog"),


    path("share_blog/", share_blog, name="share_blog"),
    # path("share_blog/<int:pk>/", share_blog, name="share_blog"),
    
    
    path("subscribe/", subscribe, name="subscribe"),
    path("unsubscribe/", unsubscribe, name="unsubscribe"),
    path("contact/", contact, name="contact"),
    path("comments/", comments, name="comments"),
    path("get_comments/", get_comments, name="get_comments"),
    path("delete_comments/<int:pk>/", delete_comments, name="delete_comments"),
    path("review/", review, name="review"),
    path("get_review/", get_review, name="get_review"),
    path("reply/", reply, name="reply"),
    path("get_reply/", get_reply, name="get_reply"),
    path("delete_reply/<int:pk>/", delete_reply, name="delete_reply"),
    path("search_blog/<str:name>/", search_blog, name="search_blog"),
]