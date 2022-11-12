from datetime import datetime, timezone

from django.db import models

# Create your models here.

class Question(models.Model):
  #definindo como o nosso model será organizado
  question_text = models.CharField(max_length=200) #variavel que recebera o texto da pergunda
  pub_date = models.DateTimeField('date_published')

  def __str__(self):
      return self.question_text

class Choice(models.Model): #pegando do Models um modelo
  question = models.ForeignKey(Question, on_delete=models.CASCADE) #toda alternativa tem que estar vinculada a uma pergunta
  #Faz o relacionamento entre a tabela Question e Choices, ou seja, para cada pergunta pode haver respostas iguais, porém identi-
  #ficadas pelo Foreignkey único de cada questão
  #on_delete=models.CASCADE -> se a pergunta for deletada, então as respostas tambmém devem ser já que estão interligadas ao
  #                            id único da questão

  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text

  #retorna as publicações recentes
  def was_published_recently(self):
    return self.pub_date >= timezone.now()-datetime.timedelta(days=1) #se for menor que um dia TRUE, se for maior FALSE


  #adicionamos a nossa aplicação polls aos settings na seção INSTALLED APPS