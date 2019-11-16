from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Serve Single Page Application
index = never_cache(TemplateView.as_view(template_name='index.html'))
Test = never_cache(TemplateView.as_view(template_name='test.html'))

#views
def post_detail(request):
    posts = Post.objects.all()
    return render(request, 'post_detail.html', {'posts': posts})
def post_view(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post_view.html', {'post': post})   

def comment_detail(request):
    comment = Comment.objects.get()
    return render(request, 'comment_detail.html')
def comment_view(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'comment_view.html', {'comment': comment})  

#new
def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            posts = form.save()
            return redirect('post_detail')
    else:
        form = PostForm()
        return render(request, 'post_form.html', {'form': form})

def comment_create(request):
    comment = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

#edit
def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('post_list')
