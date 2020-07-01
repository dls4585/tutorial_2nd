from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    #데이터베이스에서 Post의 객체들을 불러와서 posts에 저장
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    #posts 라는 문자열이 나오면 posts인거다?

