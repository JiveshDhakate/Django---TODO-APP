from django.urls import path, include
from . import views

urlpatterns = [
    path("addTask/",views.addTask, name="addTask"),
    path("markasComplete/<int:task_id>/",views.markasComplete, name="markasComplete"),
    path("markasIncomplete/<int:task_id>/",views.markasIncomplete, name="markasIncomplete"),
    path("deleteTask/<int:task_id>/",views.deleteTask, name="deleteTask"),
    path("editTask/<int:task_id>/",views.editTask, name="editTask"),
]