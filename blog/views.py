from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DeleteView, UpdateView, DetailView, CreateView
from django.core.paginator import Paginator

from .models import Post, Images
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Create your views here.


class MainPageView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user, is_delete = False)


class DetailPageView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    
    
class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add-post.html'
    fields = ['title', 'desc', 'main_image']
    success_url = reverse_lazy('main')
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # attach logged-in user
        return super().form_valid(form)

    

class EditPostView(UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    fields = ['title', 'desc', 'main_image']
    success_url = reverse_lazy('main')

    
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('main')