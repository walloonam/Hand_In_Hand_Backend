from django.urls import path
from post import views


urlpatterns = [
    path('area/create', views.create_area, name='area-create'),
    path('area/<int:pk>/delete', views.delete_area, name='area-delete'),
]