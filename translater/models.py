from django.db import models
from django.conf import settings
import hashlib


class myString(models.Model):
    original = models.TextField()
    languageTo =  models.CharField(choices=settings.LANGUAGES,max_length=150)
    translated = models.TextField()
    ident = models.CharField(max_length=128,editable=False)


    def save(self, *args, **kwargs):
        self.ident = hashlib.md5(self.original).hexdigest()
        super(myString,self).save(*args, **kwargs)
        

    def __unicode__(self):
        return "%s / %s " % (self.original,self.translated)

    
