from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    BLOG_CHOICE = [
        ('web', 'Web development'),
        ('mobile', 'Mobile development'),
        ('data', 'Data science'),
        ('AI', 'Artificial intelligence'),
        ('ML', 'Machine learning'),
        ('os', 'Opearting system'),
        ('CN', 'Computer Network'),
        ('DB', 'Database'),
        ('DS', 'Data Structures'),
        
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length=6, choices = BLOG_CHOICE)
    description = models.TextField(default = '')

    def __str__(self):
        return self.name



# Relationship models in Django 
# One to One relationship
class BlogTopic(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    description = models.TextField(default = '')
    publication_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.topic



# One to Many (ex - One blog has multiple reviews)
class BlogReview(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name = "reviews")    
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.blog.name}"



# Many to Many relationship
class Sites(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    blog_types = models.ManyToManyField(Blog, related_name = 'Sites')

    def __str__(self):
        return self.name
