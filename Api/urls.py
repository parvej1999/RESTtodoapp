from django.urls import path
from . import views

urlpatterns = [
    path("", views.taskIndex,  name = 'taskIndex'),
    path("create/", views.taskCreate,  name = 'taskCreate'),
    path("detail/<str:pk>/", views.taskDetail,  name = 'taskDetail'),
    path("update/<str:pk>/", views.taskUpdate,  name = 'taskUpdate'),
    path("delete/<str:pk>/", views.taskDelete,  name = 'taskDelete'),


]