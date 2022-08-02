from tkinter import CASCADE
from django.db import models

class Pergunta(models.Model):
    texto_pergunta = models.TextField(max_length=200)
    def __str__(self):
        return self.texto_pergunta

class Resposta(models.Model):
    fk_id_pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_resposta = models.TextField(max_length=50)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.texto_resposta

