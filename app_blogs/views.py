from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from app_blogs.forms import BlogCreationForm, CommentForm
from app_blogs.models import Blog, Like

# Create your views here.
def blog_list_view(request):
    blog_list = Blog.objects.prefetch_related("comments__user", "likes__user").order_by('-publish_date')
    # blog_list = Blog.objects.all().order_by('-publish_date')
    context = {'blog_list': blog_list}
    return render(request, "blogs/blog_list.html", context)


def blog_detail_view(request, blog_id):
    blog = get_object_or_404(Blog.objects.prefetch_related("comments__user"), pk=blog_id)
    comments = blog.comments.all()
    likes = blog.likes.all()
    form = CommentForm()
    
    # check if the user has liked or not the blog
    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = blog.likes.filter(user = request.user).exists()
    
    if request.method == "POST":
        if request.user.is_authenticated:
            if 'like' in request.POST:
                like, created = Like.objects.get_or_create(blog=blog, user = request.user)   
                user_has_liked = True
                if not created:
                    like.delete()
                    user_has_liked = False                
                # Redirect to the same blog detail page to avoid resubmission on refresh
                return redirect('blog_detail', blog_id=blog_id)                
            else:
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.user = request.user
                    comment.blog = blog
                    comment.save()
                    form = CommentForm()
                # Redirect to the same blog detail page to avoid resubmission on refresh
                return redirect('blog_detail', blog_id=blog_id)
        else:
            return redirect(f"/accounts/login/?next={request.path}")
    else:
        form = CommentForm()
    
    context = {'blog': blog, 'comments': comments, 'likes': likes, 'form': form, 'user_has_liked': user_has_liked}
    return render(request, 'blogs/blog_detail.html', context)


@login_required
def blog_create_view(request):
    if request.method == 'POST':
        form = BlogCreationForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect("blog_list")
    else:
        form = BlogCreationForm()
    
    return render(request, "blogs/blog_create.html", {'form': form})


@login_required
def blog_edit_view(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogCreationForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect("blog_list")
    else:
        form = BlogCreationForm(instance=blog)
    
    return render(request, "blogs/blog_edit.html", {'form': form})

@login_required
def blog_delete_view(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect('blog_list')
    return render(request, "blogs/blog_delete.html", {"blog": blog})


def search_results_view(request):
    query = request.GET.get('search-query')
    blog_list = Blog.objects.filter(
        Q(title__icontains = query) | Q(author__username__icontains = query)
    )
    return render(request, "blogs/search_results.html", {'blog_list': blog_list})