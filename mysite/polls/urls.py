from django.urls import path


 #traz tudo que estiver no arquivos views
from . import views


app_name = 'polls'
#caminho que gostariamos de ver nossas urls
urlpatterns = [
  path('', views.index, name='index'), #puxamos então a nossa FUNÇÃO index como um request
  path('<int:question_id>/results/', views.results, name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]