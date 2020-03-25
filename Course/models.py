from django.db import models

# Create your models here.


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=False)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
