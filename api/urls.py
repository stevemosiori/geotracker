from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tracker/update', views.update_tracker_location, name='update_tracker_location'),
    path('tracker/register', views.register_tracker, name='register_tracker'),
]