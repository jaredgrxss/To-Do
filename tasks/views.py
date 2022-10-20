from tasks.models import Task
from django.urls import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from lists.models import List
# Create your views here.


class CreateTask(LoginRequiredMixin,generic.CreateView):
    fields = ('name','list')
    model = Task
    template_name = 'tasks/create_task.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.done = False
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('lists:list-detail',kwargs={'pk':self.object.list.pk})



class DeleteTask(LoginRequiredMixin,generic.DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    def get_success_url(self):
        list_id = self.object.list.pk
        return reverse_lazy("lists:list-detail",kwargs={'pk':list_id})

