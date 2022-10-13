from django.db import models
from django.apps import apps
from django.urls import reverse
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    information = models.TextField()
    done = models.BooleanField(False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    list = models.ForeignKey('lists.List',related_name='tasks', on_delete=models.CASCADE)


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
    

