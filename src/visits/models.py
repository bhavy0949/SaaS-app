from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # path of the page visited
    # when the page was visited

    # These are columns
    # by default an id field
    path = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    