from . import views
from django.urls import path

urlpatterns = [
    path('', views.todo_home, name='todo_home'),
    # path('details/', views.todo_details, name='details'),
    # path('delete/<int:taskid>/', views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),
    path('home/', views.task_list_view.as_view(), name='home'),
    path('details/<int:pk>/', views.task_detail_view.as_view(), name='details'),
    path('update/<int:pk>/', views.task_update_view.as_view(), name='update'),
    path('delete/<int:pk>/', views.task_delete_view.as_view(), name='delete'),
]
