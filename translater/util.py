# -*- coding: utf-8 -*-
from django.db import models


class HTemplate(models.Model):
    """
    to use in future...
    """
    dateCreated = models.DateField(auto_now_add=True,editable=False)
    lastUpdated = models.DateTimeField(auto_now=True,editable=False)
    rawLog = models.TextField(blank=True,editable=False)

    class Meta:
        abstract = True


