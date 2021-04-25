from django import forms
from .models import Post, Koment
from django.contrib.auth.mixins import LoginRequiredMixin


class PostForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titull','autor','trupi',)
        widgets = {
            'titull':forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class':'select'}),
            'trupi': forms.Textarea(attrs={'class': 'form-control'}),

        }

    # def form_valid(self, form):
    #     form.instance.autor = self.request.user
    #     return super().form_valid(form)

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titull','trupi')
        widget = {
            'titull':forms.TextInput(attrs={'class': 'form-control'}),
            'trupi': forms.Textarea(attrs={'class': 'form-control'}),
        }
#
# class AddCommentForm(forms.ModelForm):
#     class Meta:
#         model = Koment
#         fields = ('body')
#