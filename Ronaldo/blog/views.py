from django.shortcuts import render, redirect
from .models import About, Home, Project, Blog, Service, Contactme, Sponsor, Category, Tag
from resume.models import Education, Experience, Awards, Skill_two, Skill_one
from comment.forms import CommentForm
from contact.forms import ContactForm
from comment.models import Comment


# Create your views here.


def index(request):
    object_home = Home.objects.all()
    object_sponsor = Sponsor.objects.all()
    object_awards = Awards.objects.all()
    object_education = Education.objects.all()
    object_experience = Experience.objects.all()
    object_skillone = Skill_one.objects.all()
    object_skilltwo = Skill_two.objects.all()
    object_about = About.objects.all()
    object_project = Project.objects.all()
    object_blog = Blog.objects.all()[:3]
    object_service = Service.objects.all()
    object_contactme = Contactme.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/#contact-section")

    context = {
        'homes': object_home,
        'edus': object_education,
        'sponsors': object_sponsor,
        'exps': object_experience,
        'awas': object_awards,
        'skillones': object_skillone,
        'skilltwos': object_skilltwo,
        'abouts': object_about,
        'projects': object_project,
        'services': object_service,
        'contactmes': object_contactme,
        'blogs': object_blog,
        'form': form,
    }

    return render(request, 'index.html', context)


def single(request, pk):
    object_blogs = Blog.objects.all()[:3]
    object_service = Service.objects.all()
    object_category = Category.objects.all()
    object_tag = Tag.objects.all()
    object_contactme = Contactme.objects.all()
    object_blog = Blog.objects.get(id=pk)
    form = CommentForm(request.POST or None)
    # object_comment = Comment.objects.all()
    url = request.META.get("HTTP_REFERER")
    if form.is_valid():
        var = form.save(commit=False)
        var.blog = object_blog
        var.save()
        return redirect(url)
    context = {
        'form': form,
        'blogs': object_blog,
        'categorys': object_category,
        'tags': object_tag,
        # 'comments': object_comment,
        'contactmes': object_contactme,
        'services': object_service,
        'recents': object_blogs,
    }

    return render(request, 'single.html', context)
