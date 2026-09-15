from django.shortcuts import render  ,get_object_or_404
from .models import Post , Category 
import datetime as dt
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import CommentForm
from .models import Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def blog_home(request,cat=None,tag=None):
    posts = Post.objects.filter(status=1 , published_date__lte = dt.date.today())
    #sort by tag and category
    cats = Category.objects.all()
    if cat:
        posts = posts.filter(category__name=cat)
    if tag:
        posts = posts.filter(tag__name=tag)
    if request.GET.get('s'):
        s = request.GET.get('s')
        posts = posts.filter(content__icontains = s )

    
    #paginator
    posts = Paginator(posts,3)
    page_number = request.GET.get("page")
    try:
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
    context = {'posts':posts , 'cats':cats  }
    return render(request,'blog/blog_home.html',context)

@login_required
def blog_single(request,pid):
    prev_post = None
    next_post = None
    post =get_object_or_404(Post , id = pid , status = 1 ,published_date__lte = dt.date.today())
    post_list =list(Post.objects.filter(status = 1 ,published_date__lte = dt.date.today()))
    post_index = post_list.index(post)
    if post_index > 0 :
        prev_post = post_list[post_index-1]
    if post_index < len(post_list)-1:
        next_post = post_list[post_index+1]

    post.counted_view = post.counted_view + 1
    post.save()

    comments = Comment.objects.filter(post=post.id , approved=True)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your comment successfully submit ,it will be published after investigations")
        else:
            messages.error(request, 'Invalid commenting.')
            messages.error(request, form.errors)
    else:
        form = CommentForm()
    context = {'post':post , 'form':form ,'comments':comments , 'next_post':next_post , 'prev_post':prev_post}
    return render(request,'blog/blog_single.html',context)


# Create your views here.
