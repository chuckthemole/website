from django.urls import path, include
from . import views
app_name = 'chucksite'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('resume', views.resume, name='resume'),
    path('projects', views.projects, name='projects')
]
