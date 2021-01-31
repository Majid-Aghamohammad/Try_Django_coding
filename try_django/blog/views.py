from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import BlogPost
# Create your views here.


def blog_post_detail_page(request, post_id):
    # obj = BlogPost.objects.get(id=post_id)
    get_object_or_404(BlogPost, id= post_id)
    template_name = 'blog_post_detail.html'
    context = {'blog_object': obj}
    return render(request, template_name, context)
    