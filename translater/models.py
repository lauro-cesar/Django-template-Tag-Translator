# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str,smart_unicode
from django.conf import settings
import hashlib
from util import HTemplate

class TranslatedString(HTemplate):
    To =  models.CharField(choices=settings.LANGUAGES,max_length=150)
    translated = models.TextField()

    def __unicode__(self):
        return self.translated

    class Meta:
        verbose_name = _(u"Texto traduzido")
        verbose_name_plural = _(u"Textos traduzidos")

class OriginalString(HTemplate):
    original = models.TextField()
    ident = models.CharField(max_length=128,editable=False)
    translations = models.ManyToManyField(TranslatedString)

    def save(self, *args, **kwargs):
        #FIXME: Just convert everything to utf-8
        # unknow original input format...

        try:
            inPut=smart_str(self.original)
        except:
            inPut=smart_unicode(self.original)


        self.ident = hashlib.md5(inPut).hexdigest()
        super(OriginalString,self).save(*args, **kwargs)


    def returnTranslated(self,To):
        #TODO: Return already translated strings
        return "None"

    def alreadyTranslated(self):
        lista=''
        for l in self.translations.select_related():
            lista+="<li>%s:%s</li>" % (l.To,l)
        return lista

    alreadyTranslated.allow_tags = True

    def __unicode__(self):
        return "%s" % (self.original)


    class Meta:
        verbose_name = _(u"Texto Original")
        verbose_name_plural = _(u"Textos originais")
