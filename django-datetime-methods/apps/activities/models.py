from django.db.models import *
from django.db import models as models


class Activity(models.Model):

    # Fields
    due_date = models.DateTimeField()

    class Meta:
        ordering = ('due_date',)

    def __unicode__(self):
        return u'%s' % self.id
