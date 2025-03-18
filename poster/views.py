from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, PostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    posts = Post.objects.all().prefetch_related('comment_set')
    return render(request, 'posts.html', {'posts': posts})
def post_list(request):
    posts = Post.objects.all().prefetch_related('comment_set')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = request.POST.get('post_id')
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()
    
    return render(request, 'posts.html', {
        'posts': posts,
        'form': form,
    })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def create_post(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
def post_list(request):
    all_posts = Post.objects.all().order_by('-id')  
    paginator = Paginator(all_posts, 5)  
    
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = request.POST.get('post_id')
            comment.save()
            return redirect(f"{request.path}?page={posts.number}")
    else:
        form = CommentForm()
    
    return render(request, 'posts.html', {
        'posts': posts,
        'form': form,
    })