from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('weather_app/', views.index, name='weather_app'),
    path('text-html-text/', views.convertor_view, name='text-html'),
    path('calories-counter/', views.calories_counter, name='calories_counter'),
    path('todo-list/', views.todo_list.as_view(), name='todo_list'),
    path('<int:todo_id>/delete', views.delete, name='todo_delete'),
    path('<int:todo_id>/update', views.update, name='todo_update'),
    path('add/', views.add, name='todo_add'),
    path('blog/', views.blog, name='blog'),
    path('create-blog/', views.blog_upload, name='blog_upload'),
    
    
]


