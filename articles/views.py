from django.shortcuts import render

from articles.models import Article
from newspapers.API import *
# Create your views here.

#def render(request,page=1):
    #return Article.objects.filter(page_id=page)


ARTICLE_FIELDS = [
    'article.title',
    'article.guid',
    'article.description',
    'article.image.guid',
    'article.image.caption',
    'article.image.urls.large',
    'article.image.width',
    'article.image.height'
]


def render(request, page):

    articles = Article.objects.filter(page_id=page)
    options = {}
    results = {}
    for article in articles:
        query = article.query
        to_date = article.to_date
        from_date = article.from_date
        page_size = article.page_size
        has_images = article.has_images
        if query:
            options['query'] = query
        if to_date:
            options['to_date'] = to_date
        if from_date:
            options['from_date'] = from_date
        if page_size:
            options['pagesize'] = page_size
        if has_images:
            options['has_images'] = has_images

        options['fields'] = ' '.join(ARTICLE_FIELDS)

        article_obj = NewscredApi('articles', options)
        results[article.block_choice] = article_obj.response()
    return results

def render_article(request):
    main_article_response = NewsCredApiArticle(guid="455b8927849a54bd5d953a4b0fde0a5e").response()
    #import pdb;pdb.set_trace();
    return main_article_response