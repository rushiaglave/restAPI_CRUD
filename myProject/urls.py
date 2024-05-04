from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task-list/', views.tasklist, name='task-list'),
    path('task-create/', views.taskcreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskupdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskdelete, name='task-delete')

]
