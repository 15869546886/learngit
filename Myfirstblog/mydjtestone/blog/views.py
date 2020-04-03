from django.shortcuts import render
from .models import BlogArticles
from django.contrib.auth.decorators import login_required
from .forms import BlogArticlesForm
from django.http import HttpResponse


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,'blog/title.html',{'blogs':blogs})

def blog_article(request):
    article = BlogArticles.objects.get(id='article_id')
    pub = article.publish
    return render(request,'blog/content.html',{'article':article,'publish':pub})

@login_required()
def blog_post(request):
    if request.method == 'GET':
        blog_form = BlogArticlesForm()
        return render(request,'blog/blog_post.html',{'blog_form':blog_form})
    if request.method == 'POST':
        blog_form = BlogArticlesForms(request.POST)
        if blog_form.is_valid():
            cd = blog_form.cleaned_data
            try:
                new_blog = blog_form.save(commit=False)
                new_blog.author = request.user
                new_blog.save()
                return HttpResponse('1')
            except:
                return HttpResponse('-1')
        else:
            return HttpResponse('0')

