from django import forms

from .models import Post


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "block w-full p-3 rounded bg-gray-200 border border-transparent focus:outline-none",
                                                                       "placeholder": "Post"}), required=True)
    
    
    class Meta:
        model = Post
        fields = ['title', 'body',]

class PostEditForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "block w-full p-3 rounded bg-gray-200 border border-transparent focus:outline-none",
                                                                       "placeholder": "Post"}), required=True)

    class Meta:
        model = Post
        fields = ('body',)