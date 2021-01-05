from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Blog
from .forms import BlogForm

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Blog.objects.all()


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = BlogForm
    queryset = Blog.objects.all()
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    # queryset = Blog.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blog, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = BlogForm
    queryset = Blog.objects.all()
    success_url = '/blog'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blog, id=id_)

    def form_valid(self, form):
        return super().is_valid(form)


class ArticleDeletelView(DeleteView):
    template_name = 'blog/article_delete.html'
    success_url = '/blog/'
    # queryset = Blog.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blog, id=id_)
