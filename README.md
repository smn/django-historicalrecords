Django Historical Records
=========================

This is from Marty Alchin's [Pro Django](http://prodjango.com/) book.

Setup the virtualenv

    $ virtualenv --no-site-packages ve
    $ source ve/bin/activate
    (ve)$ pip install -r requirements.pip
    

Import the HistoricalRecords and attach it to your model like you would a custom Django manager.

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

If you run `manage.py syncdb` you'll see that it automatically creates a `Historical` version of whatever model you've attached it to.

    (ve)$ ./manage.py syncdb
    Creating table auth_permission
    ... // snip // ...
    Creating table example_app_historicaltestmodel <- HistoricalTestModel!
    Creating table example_app_testmodel
    ... // snip // ...

The `HistoricalRecords` clone the model it is attached to and adds some extra fields that allow you to track the type of change made, the timestamp of when the change was saved and it has a descriptor that will return the original object at the time of the change.

    (ve)$ ./manage.py shell
    >>> from example_app.models import TestModel
    >>> tm = TestModel.objects.create(boolean=True,characters="abc")
    >>> tm.history.count()
    1
    >>> most_recent = tm.history.most_recent()
    >>> most_recent.boolean
    True
    >>> most_recent.characters
    u'abc'
    >>> tm.boolean = False
    >>> tm.characters = "def"
    >>> tm.save()
    >>> tm.history.count()
    2
    >>> tm.history.all()
    [<HistoricalTestModel: TestModel as of 2010-09-10 03:29:59.424761>, <HistoricalTestModel: TestModel as of 2010-09-10 03:28:31.358548>]
    >>> from datetime import datetime
    >>> timestamp = datetime(2010,9,10,3,28,31,358548)
    >>> old_version = tm.history.as_of(timestamp)
    >>> old_version.boolean
    True
    >>> tm.boolean
    False
    >>> old_version.characters
    u'abc'
    >>> tm.characters
    'def'
    >>> 
    
