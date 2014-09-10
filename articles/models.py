from django.db import models
from pages.models import Page


# Create your models here.

class Article(models.Model):
    page_id = models.ForeignKey(Page)
    query = models.CharField( max_length= 25)
    from_date = models.DateTimeField( null= True, blank= True)
    to_date = models.DateTimeField(null= True, blank= True)
    page_size = models.IntegerField( null= True, blank= True)
    has_images= models.BooleanField(bool)

    class Meta:
        db_table = 'articles'