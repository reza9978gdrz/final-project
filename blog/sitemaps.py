from django.contrib.sitemaps import Sitemap
from .models import Post

class BlogSitemap(Sitemap):
    changefreq = "mounthly"
    priority = 0.5
    
    def items(self):
        posts = Post.objects.filter(status=1)
        return posts
      
    def lastmod(self, obj):
        return obj.published_date