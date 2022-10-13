from django.urls import path
from lists import views
app_name = 'lists'

urlpatterns = [
    path('myList/',views.ListLists.as_view(),name='show-list'),
    path('createList/',views.CreateList.as_view(),name='create-list'),
    path('deleteList/<int:pk>',views.DeleteList.as_view(),name='delete-list'),
    path('updateList/<int:pk>',views.UpdateList.as_view(),name='update-list'),
    path('detailList/<int:pk>',views.DetailList.as_view(),name='list-detail'),
]