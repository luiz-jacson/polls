from tkinter import CASCADE
from django.db import models

class Pergunta(models.Model):
    texto = models.TextField(max_length=200)
    def __str__(self):
        return self.texto

class Resposta(models.Model):
    id_pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.TextField(max_length=50)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.texto

