from django.shortcuts import *
from pages.forms import ContactForm
from pages.functions import paginate
from pages.models import ContactModel,Content,Category,Tag
from users.models import Reviews
from django.contrib import messages
from django.http import JsonResponse
from django.core.files import storage
# Create your views here.

def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success=f"Your message has been sent. we will reach out to you as soon as possible..."
            messages.success(request, success)
            return HttpResponseRedirect("/")
    services = Content.objects.filter(category__name='Services')[:3]
    gallery = Content.objects.filter(category__name='gallery')[:4]
    reviews = Reviews.objects.filter()[:3]
    context = {
        "form": form,
        "title":"homepage",
        "services":services,
        "gallery":gallery,
        "reviews":reviews,
    }
    return render(request,"homepage.html",context)

def about(request):
    context = {
        "title":"about",
    }
    return render(request,"homepage.html",context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Form submitted successfully!',"errors":""})
        else:
            return JsonResponse({'message': "errors","errors":form.errors}, status=200)
    context = {
        "title":"contact",
        "form": form,
    }
    return render(request,"homepage.html",context)

def services(request):
    services = Content.objects.filter(category__name='Services')
    contents = paginate(services,request.GET.get('page'),10)
    context = {
        "services":contents,
        "title":"services",
    }
    return render(request,"homepage.html",context)

def reviews(request):
    reviews = Reviews.objects.filter()
    contents = paginate(reviews,request.GET.get('page'),10)
    context = {
        "title":"reviews",
        "reviews":contents,
    }
    return render(request,"homepage.html",context)

def gallery(request):
    gallery = Content.objects.filter(category__name='gallery')
    contents = paginate(gallery,request.GET.get('page'),10)
    context = {
        "title":"gallary",
        "gallery":contents,
    }
    return render(request,"homepage.html",context)

def service_view(request,service_slug=''):
    content = Content.objects.filter(category__name='Services',slug=service_slug).first()
    if not content:
        return render(request=request,template_name="404.html")
    context = {
        "title":content.title,
        "content":content,
    }
    return render(request,"page.html",context)

def pages_view(request,page_slug):
    content = Content.objects.filter(category__name='pages',slug=page_slug).first()
    if not content:
        return render(request=request,template_name="404.html")
    context = {
        "title":content.title,
        "content":content,
    }
    return render(request,"page.html",context)

def json_pages_view(request,category,page_slug):
    content = Content.objects.filter(category__name=category,slug=page_slug).first()
    if not content:
        return render(request=request,template_name="404.html")
    context = {
        "title":content.title,
        "content":content.description,
        "category": category,
        "slug": content.slug, 
        "price":  content.price,
        "created_at": content.created_at, 
        "updated_at": content.updated_at, 
    }
    return JsonResponse(context)
