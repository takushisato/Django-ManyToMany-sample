from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog


class BlogView(TemplateView):

    def get(self, request, *args, **kwargs):
        # IDを指定して一つ取り出し
        # blog = Blog.objects.get(id=1)
        # all_tags = blog.tags.all()

        # タグのIDを指定して全件取り出し
        blog = Blog.objects.prefetch_related('tags').get(id=2)

        # これは動かない
        blog = Blog.objects.select_related('title').get(id=2)


        return render(request, 'index.html', {
            'blog': blog,
            # 'all_tags': all_tags
        })

# https://www.northtorch.co.jp/archives/1151
# prefetch_related()とselect_related()
