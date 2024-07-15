from django.urls import path
from . import views

# . -> means current directory 


urlpatterns = [
    path('', views.all_demo, name = "all_demo"), #  name = "Home" -> This is optional parameter

    # http://127.0.0.1:8000/demo/1/
    path('<int:blog_id>/', views.blog_detail, name = "blog_detail"),

    # http://127.0.0.1:8000/demo/blog_site/
    path('blog_site/', views.blog_site, name = "blog_site"),
    
]  