from django.forms import ModelForm, TextInput, Select, Textarea
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('user', 'title', 'description', 'category', 'publish')

        widgets = {
            # 'user': Select(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            # 'description': Textarea(attrs={'class': 'form-control'}),
            'category': TextInput(attrs={'class': 'form-control'}),
            'publish': TextInput(attrs={'class': 'form-control'})
        }