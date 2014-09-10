from django.db import models
from pages.models import Page

# Create your models here.
class Images(models.Model):
    page_id = models.ForeignKey(Page)
    query=models.CharField(max_length=25)
    from_date= models.DateTimeField(null=True,blank=True)
    to_date=models.DateTimeField(null=True,blank=True)
    page_size =models.IntegerField(null=True, blank=True)


    class Meta:
        db_table= 'images'