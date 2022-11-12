from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Question
# Create your views here.


#criaremos uma pagina inicial para esta aplicacao

def index(request): #utilizamos o request sempre que precisamos fazer uma requisição para o site mencionado
  latest_question_list = Question.objects.order_by("-pub_date")[:5] #pega as ultimas 5 questions
  context = {"latest_question_list": latest_question_list}
  return render(request, 'polls/index.html', context)

#precisamos setar a aplicacao a uma URL para conseguirmos realizar o request, criamos então o arquivo urls.py dentro da nossa
#pasta da aplicacao polls


#Queremos ter agora, uma view que mostra quais são as perguntas do nosso sistema
#Queremos ter também uma view que ao clicar em uma pergunta, mostrar as alteranativas para  votar]

#Outra vieww mostrando os resultados obtidos das votações anteriores

def results(request, question_id):
  question = Question(pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except KeyError:
    return render(request, 'polls/vote.html', {
      'question': question,
      'error_message': "You didn't select a choice",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

