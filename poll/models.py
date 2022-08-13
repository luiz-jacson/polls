from django.db.models.deletion import CASCADE
from django.db import models
from django.urls import reverse

class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=200)
    def __str__(self):
        return self.texto_pergunta

class Resposta(models.Model):
    fk_id_pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_resposta = models.CharField('Answers', max_length=50)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.texto_resposta
   

