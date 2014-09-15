from django.db import models
from pages.models import Page

# Create your models here.

class Flicker(models.Model):
    page_id = models.ForeignKey(Page)
    text = models.CharField( max_length = 255 )
    per_page = models.IntegerField()

    class Meta:
        db_table= 'flicker'