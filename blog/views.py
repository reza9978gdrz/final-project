from django.shortcuts import render , HttpResponse
from .models import Post , Category , Tag
import datetime as dt
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import CommentForm
from .models import Comment

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
        posts = posts.filter()

    tags = Tag.objects.all()
    #paginator
    posts = Paginator(posts,3)
    page_number = request.GET.get("page")
    try:
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
    context = {'posts':posts , 'cats':cats , 'tags':tags }
    return render(request,'blog/blog_home.html',context)

def blog_single(request,pid):
    post = Post.objects.get(pk=pid)
    count = post.counted_view
    count = count + 1
    post.counted_view = count
    post.save()
    title = post.title
    comments = Comment.objects.filter(post=title)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/')
    else:
        form = CommentForm()
    context = {'post':post , 'form':form ,'comments':comments}
    return render(request,'blog/blog_single.html',context)

# Create your views here.
