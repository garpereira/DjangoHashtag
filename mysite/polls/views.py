from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#criaremos uma pagina inicial para esta aplicacao

def index(request): #utilizamos o request sempre que precisamos fazer uma requisição para o site mencionado
  return HttpResponse ("Olá este é o index")

#precisamos setar a aplicacao a uma URL para conseguirmos realizar o request, criamos então o arquivo urls.py dentro da nossa
#pasta da aplicacao polls