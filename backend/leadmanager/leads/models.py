from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    message = models.CharField(max_length=600, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



