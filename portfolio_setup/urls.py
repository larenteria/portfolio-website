from django.urls import path
from . import views

# URL Conf module
urlpatterns = [
    path('', views.home, name='home'),
    path('chess', views.chess, name='chess'),
    path('dataScraper', views.dataScraper, name='dataScraper'),
    path('imageScrambler', views.imageScrambler, name='imageScrambler'),
    path('resume', views.resume, name='resume')
    ]
