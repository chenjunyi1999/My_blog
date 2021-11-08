from django import forms
# 引入文章模型
from .models import ArtcilePost

# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArtcilePost
        # 定义表单包含的字段
        fields = ('title', 'body', 'tags', 'avatar')