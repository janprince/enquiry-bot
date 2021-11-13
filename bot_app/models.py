from django.db import models


# Create your models here.
class Response(models.Model):
    response_text = models.TextField(blank=True)
    keyboard_options = models.CharField(max_length=500)  # this


class Command(models.Model):
    command = models.CharField(max_length=255, blank=True)
    response = models.ForeignKey(Response, null=True, on_delete=models.SET_NULL, related_name="comma")
