from django.urls import path
from . import views

urlpatterns = [
path('',views.home, name='home'),
path('create/', views.create, name='create'),
path('<int:startup_id>/get_photo', views.get_photo, name='get_photo'),
path('<int:startup_id>/add_photo/', views.add_photo, name='add_photo'),
path('<int:startup_id>/update/', views.update, name='update'),
path('<int:startup_id>/delete/', views.delete, name='delete'),

]
