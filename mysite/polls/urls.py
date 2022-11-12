from django.urls import path


 #traz tudo que estiver no arquivos views
from . import views

#caminho que gostariamos de ver nossas urls
urlpatterns = [
  path('', views.index, name='index')
]