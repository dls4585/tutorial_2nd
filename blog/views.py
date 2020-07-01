from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    #데이터베이스에서 Post의 객체들을 불러와서 posts에 저장
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    #posts 라는 문자열이 나오면 posts인거다?

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    # request.POST에 우리가 입력한 데이터들이 저장된다
    if request.method == "POST":
        form = PostForm(request.POST) #받은 데이터를 PostForm으로 넘겨주기
        if form.is_valid():
            post = form.save(commit=False) #넘겨진 데이터를 모델에 바로 저장하지 마라
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #form <- PostForm with 우리가 받은 데이터
            #PostForm <- Post 모델을 사용, request.POST의 데이터를 받아옴
            #post <- form의 데이터를 넘겨받음
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})