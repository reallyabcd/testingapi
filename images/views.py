from django.views.generic import ListView
from django.http import JsonResponse
from .models import *
from django.shortcuts import render
# Create your views here.

class ImageListView(ListView):
    model = Image
    template_name = 'images/all_images.html'

def Imagelist(request):
    cat = Category.objects.all()
    context = {
        'list':cat,
    }
    return render(request, 'images/list.html', context)

#return json for categories
def json(request):
    data = list(Category.objects.values())
    return JsonResponse(data, safe=False)

def get_image_by_category(category_id):
    images = Image.objects.filter(category__id=category_id)
    return images

def get_category_images(request, category_id):
    category = Category.objects.get(id=category_id)
    images = get_image_by_category(category_id)
    return render(request, 'images/filtered_images.html', {'category': category, 'images':images})

#returning json for every image
def Images_json(request):
    data = list(Image.objects.values())
    return JsonResponse(data, safe=False)