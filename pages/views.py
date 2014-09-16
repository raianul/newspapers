from django.shortcuts import render

from gallery.views import render as gallery_render
from articles.views import render as article_render
from video.views import render as video_render
from articles.views import render_article as main_article_render
from flicker.views import render as flicker_render
from topic.views import render as topic_render

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

    context_dict = {}
    gallery = gallery_render(request, request.page.pk)
    image_count = 0
    if gallery:
        images = gallery['image_set']
        image_count  =  gallery['num_found']
        context_dict['images'] = images
        context_dict['image_count'] = image_count
        context_dict['request_page_name']=request.page

    articles= article_render(request, 1)
    article_count = 0
    if articles:
        articles =articles['article_set']
        article_count= articles['num_found']
        context_dict['articles'] = articles
        context_dict['article_count'] = article_count

    videos= video_render(request, 1)
    video_count = 0
    if videos:
        videos =videos['video_set']
        video_count= videos['num_found']
        context_dict['videos'] = videos
        context_dict['video_count'] = video_count

    flickers = flicker_render(request, request.page.pk)
    
    if flickers:
        context_dict['flickers'] = flickers['photos']['photo']

    topics = topic_render(request, request.page.pk)
    if topics:
        context_dict['topics'] = topics['topic_set']


    #if (request.page=="Article Paage"):
    #    main_article=article_render(request)

    if request.page_params:
        template = 'post.html'
        response_main_article = main_article_render(request)
        context_dict['description']=response_main_article['article']['description']
        context_dict['topic']=response_main_article['article']['topic_set'][0]['description']

    else:
        template = 'index.html'

    return render(request, template , context_dict )
