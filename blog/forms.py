from django import forms
from .models import Post, Comment

#우리가 만드는 폼의 이름 그리고 이 폼이 ModelForm이라고 장고에게 알려주기
class PostForm(forms.ModelForm):
    #이 폼을 만들기 위해서 어떤 모델이 쓰이는지
    #장고가 약속해놓은거 class Meta로 쓰자
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)