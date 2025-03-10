from django.urls import path
from . import views 
app_name = "todolist"
urlpatterns = [
    path('',views.index,name='index'),
    path('select_day',views.select_day,name='select_day'),
    path('detail/<str:date>',views.detail,name='detail'),
    path('detail/<str:date>/<int:num>',views.detail,name='detail'),
    path('create/<str:date>',views.create,name='create'),
    path('delete/<str:date>',views.delete,name='delete'),
    path('signup', views.signup_view, name='signup'),
]


