from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

from .models import BlogPost
# Form classes
class BlogForm(forms.Form):
    blogTitle = forms.CharField(label='Title', max_length=64, widget=forms.TextInput(attrs={'required': True}))
    blogContent = forms.CharField(label='Content', max_length=10000, widget=forms.Textarea(attrs={'class': 'composeContent', 'required': False}))

# Create your views here.
def index(request):
    return HttpResponse('hello')

def compose(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = BlogPost(title=form.cleaned_data['blogTitle'], content=form.cleaned_data['blogContent'])
            post.save()
            return HttpResponseRedirect(reverse('blogpage'))
            
    return render(request, 'blog/compose.html', {
        'composeForm': BlogForm()
    })

def store_data(request):
    return render(request, 'blog/blogpage.html', {
        'blogPosts': BlogPost.objects.all()
    })

def show_fullpost(request, blog_id):
    return render(request, 'blog/fullpost.html', {
        'fullPost': BlogPost.objects.get(id=blog_id)
    })