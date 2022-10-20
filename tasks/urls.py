from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('delete/<int:pk>',views.DeleteTask.as_view(),name='delete-task'),
    path('create/',views.CreateTask.as_view(),name='create-task')
]