from django.shortcuts import render 
from django.http import HttpResponse 
from core.models.page import StaticPage 


def index_view(request):
    return render(request, 'core/index.html', status=200)


def about_view(request):
    try:
        page = StaticPage.objects.filter(slug='gioi-thieu').first()
    except Exception as e:
        page = False 

    if page:
        return render(request, 'base_static_page.html', page.content, status=200)
    else:
        return render(request, 'about.html', status=200)
    

def contact_view(request):
    try:
        page = StaticPage.objects.filter(slug='lien-he').first()
    except Exception as e:
        page = False 

    if page:
        return render(request, 'base_static_page.html', page.content, status=200)
    else:
        return render(request, 'contact.html', status=200)
    

def product_by_category_view(request, category_slug):
    pass 


def product_detail_view(request, category_slug, product_slug):
    pass 


def static_page_view(request, slug):
    try:
        page = StaticPage.objects.filter(slug=slug).first()
    except Exception as e:
        page = False 

    if page:
        return render(request, 'base_static_page.html', page.content, status=200)
    else:
        return HttpResponse('<h1>404 Not Found</h1>', status=404)