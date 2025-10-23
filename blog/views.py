from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.paginator import Paginator

from .models import Post, Images
from django.shortcuts import get_object_or_404

# Create your views here.


class MainPageView(View):
    def get(self, request):
        return render(request, 'blog/index.html',{'posts':Post.objects.filter(is_delete = False)})


class DetailPageView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug = slug)
        images = Images.objects.filter(post = post)
        return render(request, 'blog/detail.html', {'post':post, 'images':images})
    
    
class AddPostView(View):
    def get(self, request):
        return render(request, 'blog/add-post.html')
    
    def post(self, request):
        
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        main_image = request.FILES['main_image']
        
        Post.objects.create(
            title=title,
            desc=desc,
            main_image=main_image,
        )
        
        return redirect('/')
    

class EditPostView(View):
    def get(self, request, slug):
        return render(request, 'blog/edit.html', context={'post' : Post.objects.get(slug = slug)})
    

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        title = request.POST.get('title')
        desc = request.POST.get('desc')
        main_image = request.FILES.get('main_image')

        # Update fields if they are present in the request
        if title:
            post.title = title
        if desc:
            post.desc = desc
        if main_image:
            post.main_image = main_image

        post.save()
        return redirect('/')
    
    
class DeletePostView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('/')