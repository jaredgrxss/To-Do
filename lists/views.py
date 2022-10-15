from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from psutil import users
from lists.models import List
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
# Create your views here.
User = get_user_model()
class ListLists(LoginRequiredMixin,generic.ListView):
    model = List
    template_name = 'lists/list_lists.html'
    login_url = 'accounts:login'
    context_object_name = 'current_lists'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user = self.request.user)


class DetailList(LoginRequiredMixin,generic.DetailView):
    template_name = 'lists/list_detail.html'
    model = List


class CreateList(LoginRequiredMixin,generic.CreateView):
    template_name = 'lists/create_list.html'
    fields = ('name','description')
    model = List
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeleteList(LoginRequiredMixin,generic.DeleteView):
    template_name = 'lists/delete_list.html'
    model = List
    success_url = reverse_lazy('lists:show-list')

class UpdateList(LoginRequiredMixin,generic.UpdateView):
    template_name = 'lists/update_list.html'
    fields = ('name','description')
    model = List
       





