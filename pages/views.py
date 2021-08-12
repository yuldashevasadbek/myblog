from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'barcha_postlar'

class AboutPageView(TemplateView):
    template_name = 'about.html'
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
class NewPost(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields= ['title','author','text',]
class PostEdit(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text']
class DeletePost(DeleteView):
    model = Post
    template_name='post_delete.html'
    success_url = reverse_lazy('home')
