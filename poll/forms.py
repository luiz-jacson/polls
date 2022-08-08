from dataclasses import fields
from django import forms
from .models import Resposta, Pergunta

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['texto_resposta']

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = '__all__'