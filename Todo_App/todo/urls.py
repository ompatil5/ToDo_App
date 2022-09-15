from django.urls import path
from . import views

urlpatterns = [
    path('',views.alltask, name = 'alltask'),
    path('task_detail/<int:pk>/',views.task_detail_page,name = 'task_detail'),
    path('task/<int:pk>/delete/',views.delete_task, name = 'delete_task'),
    path('task/<int:pk>/update/',views.update_task, name = 'update_task'),

]