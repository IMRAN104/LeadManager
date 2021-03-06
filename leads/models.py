from django.db import models


# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    message = models.CharField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
