from django.shortcuts import render
from .models import Blog, Sites
from django.shortcuts import get_object_or_404
from .forms import BlogForm

# Create your views here.
def all_demo(request):
    blogs = Blog.objects.all()
    return render(request, 'demoapp.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})


def blog_site(request):
    sites = None
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_title = form.cleaned_data('blog_title')
            Sites.objects.filter(blog_types = blog_title)
    else:
        form = BlogForm()
    return render(request, 'blog_site.html', {'sites': sites, 'form': form})