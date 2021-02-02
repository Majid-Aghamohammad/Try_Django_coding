from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import BlogPost
from .Create_Form import CreatePostForm
# Create your views here.


# def blog_post_detail_page(request, post_id):
#     # obj = BlogPost.objects.get(id=post_id)
#     obj = get_object_or_404(BlogPost, id= post_id)
#     template_name = 'blog_post_detail.html'
#     context = {'blog_object': obj}
#     return render(request, template_name, context)


def blog_post_create_view(request):
    form = CreatePostForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
    template_name = 'blog_post_create.html'
    context =  {'form' : form } 
    return render(request, template_name, context)



def blog_post_list_view(request):
    obj = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    print(obj)
    context = {'objects_list': obj}
    return render(request, template_name, context)



def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog_post_detail.html'
    context = {'blog_object': obj}
    return render(request, template_name, context)



def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = CreatePostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'blog_post_update.html'
    context = {'form': form}
    return render(request, template_name, context)



def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog_post_detail.html'
    context = {'blog_object': obj}
    return render(request, template_name, context)

