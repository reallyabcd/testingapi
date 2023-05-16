from django.urls import path
from django.views.generic import TemplateView
from .views import ImageListView
app_name = 'images'
from .import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="images/index.html")),
    path('wallpapers/', ImageListView.as_view(), name='images'),
    path('categories/',  views.Imagelist, name="Imagelistt"),
    #jsons

    path('images/<int:category_id>/', views.get_category_images, name="get_category_images"),
    path('category_json/', views.json, name='json'),
    path('image_json/', views.Images_json, name="Image_json"),
]