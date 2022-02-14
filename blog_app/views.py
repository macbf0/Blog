from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.publisehd.all()
    return render(request, 'blog_app/post/list.html',{'posts': posts})


def post_detail(request, post, day, month, year):
    post = get_object_or_404(Post, label=post,status='publicado',publish_year=year, publish_month=month, publish_day=day )
    return render(request, 'blog_app/post/detail.html', {'post':post})