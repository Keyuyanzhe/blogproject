from django.contrib.syndication.views import Feed

from .models import Post

class AllPostRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "可与言者"

    # 通过聚合阅读器跳转到网页的地址
    link = "/"

    # 显示在聚合阅读器上的描述信息
    description = "个人博客"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body
