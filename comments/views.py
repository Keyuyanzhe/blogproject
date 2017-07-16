from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    # 先获取被评论的文章，将评论和被评论的文章关联起来
    post = get_object_or_404(Post, pk=post_pk)

    # 通过post请求提交数据
    if request.method == 'POST':
        # 构造CommentForm实例，生成表单
        form = CommentForm(request.POST)
        
        # 判断数据是否合法
        if form.is_valid():
            # 利用表单的数据生成comment模型类的实例，但还不保存评论到数据库
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来
            comment.post = post

            # 将数据保存进数据库
            comment.save()

            # 重定向到 get_absolute_url 方法返回的URL
            return redirect(post)

        else:
            # 数据不合法，重新渲染详情页，并且渲染表单的错误
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                      }
            return render(request, 'blog/detail.html', context=context)
    # 不是post请求，重定向到文章详情页
    return redirect(post)

