from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('binary/', views.binary, name='binary'),
    path('form/', views.form, name='form'),
    path('generate/', views.generate, name='generate'),
    path('geog/', views.geog, name='geog'),
    path('stress/', views.stress, name='stress'),
    path('typemaster/', views.typemaster, name='typemaster'),
]