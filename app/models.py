from django.conf import settings
from django.db import models

class Place(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visit_date = models.DateField()
    coordinates = models.CharField(max_length=50)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
