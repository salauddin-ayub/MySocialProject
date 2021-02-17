from django import forms
from django.forms import models
from AppPosts.models import Post

class PostForm(models.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"