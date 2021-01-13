from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html' , { 'posts' : posts })
# 변수명이 정의되지 않았다면 = 를 사용하지 않았다는 것이다

