from tasks.models import Task
from audioop import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class CreateTask(LoginRequiredMixin,generic.CreateView):
    fields = ('')



class DeleteTask(LoginRequiredMixin,generic.DeleteView):
    model = Task
    def get_success_url(self):
        list_id = self.kwargs['pk']
        return reverse_lazy("lists:list-detail",kwargs={'pk':list_id})

