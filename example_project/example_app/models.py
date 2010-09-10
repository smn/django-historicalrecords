from django.db import models
from history.models import HistoricalRecords

class TestModel(models.Model):
    """A model for testing"""
    boolean = models.BooleanField(default=True)
    characters = models.CharField(blank=True, max_length=100)
    
    history = HistoricalRecords()
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"TestModel"
