from django.db import models

# Create your models here.

class Page(models.Model):
    page_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'pages'

    def __unicode__(self):
        return self.name