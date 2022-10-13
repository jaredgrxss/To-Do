from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class List(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name='lists',on_delete=models.CASCADE)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list-detail", kwargs={"pk": self.pk})



