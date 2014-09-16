from django.shortcuts import render

from articles.models import Article
from newspapers.API import *
# Create your views here.

#def render(request,page=1):
    #return Article.objects.filter(page_id=page)


def render(request,page):
    ## galleris = to get the all galleries by using Gallery model class . .query
    try:
        article = Article.objects.filter(page_id=page)[0]
    except IndexError:
        return False
    options = {}

    query = article.query
    to_date = article.to_date
    from_date = article.from_date
    page_size = article.page_size
    has_images = article.has_images
    if query:
        options['query'] = query
    if to_date:
        options['to_date'] =to_date
    if from_date:
        options['from_date'] =from_date
    if page_size:
        options['page_size'] =page_size
    if has_images:
        options['has_images'] =has_images

    article_obj = NewscredApi('articles', options)
    return article_obj.response()

def render_article(request):
    main_article_response = NewsCredApiArticle(guid="455b8927849a54bd5d953a4b0fde0a5e").response()
    #import pdb;pdb.set_trace();
    return main_article_response

