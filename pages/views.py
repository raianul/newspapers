from django.shortcuts import render
from gallery.views import render as gallery_render
# Create your views here.

def home(request):
    gallery = gallery_render(page=1)
    return render( request, 'index.html' , {} )
