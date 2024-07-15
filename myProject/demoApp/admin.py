from django.contrib import admin
from .models import Blog, BlogTopic, BlogReview, Sites
# Register your models here.


class BlogReviewInline(admin.TabularInline):
    model = BlogReview
    extra = 2 # add field 

# modify the admin panel
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [BlogReviewInline]

class SitesAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    filter_horizontal = ('blog_types', )

class BlogTopicAdmin(admin.ModelAdmin):
    display_list = ('topic', 'description')
   

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogTopic, BlogTopicAdmin)
admin.site.register(Sites, SitesAdmin)

