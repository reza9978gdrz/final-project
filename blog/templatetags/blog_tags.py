from django import template
from blog.models import Post ,Category ,Comment
import datetime as dt

register = template.Library()

@register.simple_tag(name='comment_number')
def comment_number(pid):
    post = Post.objects.get(pk=pid)
    number = Comment.objects.filter(post=post).count()
    return number


@register.inclusion_tag('blog/blog_recent_post.html')
def recent_posts():
    posts = Post.objects.filter(status=1, published_date__lte=dt.date.today()).order_by('-created_date')[:3]
    return {'posts':posts}

@register.inclusion_tag('blog/blog_categories.html')
def categories():
    cats = Category.objects.all()
    return {'cats':cats}