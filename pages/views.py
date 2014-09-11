from django.shortcuts import render
from gallery.views import render as gallery_render
from articles.views import render as article_render
from video.views import render as video_render

# Create your views here.
 #Raiyan vai's part
'''def home(request):
    gallery = gallery_render(request, 1)
    images = gallery['image_set']
    count  =  gallery['num_found']
    return render(request, 'index.html' , {'images': images, 'count': count} )
##here create for content,video as like images as well'''

#follow gallery files

def home(request):
    gallery = gallery_render(request, 1)
    image_count = 0
    if gallery:
        images = gallery['image_set']
        import pdb; pdb.set_trace()
        image_count  =  gallery['num_found']


    articles= article_render(request, 1)
    article_count = 0
    if articles:
        articles =articles['article_set']
        article_count= articles['num_found']

    videos= video_render(request, 1)
    video_count = 0
    if videos:
        videos =videos['video_set']
        video_count= videos['num_found']

    return render(request, 'index.html' , {'images': images, 'image_count': image_count, 'articles': articles, 'article_count': article_count, 'videos': videos, 'video_count': video_count} )