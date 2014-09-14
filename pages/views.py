from django.shortcuts import render
#from pages.MiddleWare import LocalMiddleWare
from newspapers.settings import MIDDLEWARE_CLASSES
# Create your views here.

def home(request):
    #import pdb; pdb.set_trace()
    #setattr()

    return render( request, 'index.html' , {'name':'1234567890'})
