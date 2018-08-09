from django.db import models
from tinymce.models import HTMLField


class Entry(models.Model):
    entryId = models.AutoField(primary_key=True, editable=False)
    entryTitle = models.CharField(verbose_name=u"Post Title", max_length=70)
    entrySlug = models.SlugField(unique=True)
    entryText = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.entryTitle
        
    class Meta:
        ordering = ["-created"]
