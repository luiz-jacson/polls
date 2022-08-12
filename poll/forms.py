from dataclasses import fields
from django import forms
from .models import Resposta, Pergunta

class RespostaForm(forms.ModelForm):
    texto_resposta = forms.CharField(label='Answers',max_length=50,required=True)
    class Meta:
        model = Resposta
        fields = ['texto_resposta']
    

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = '__all__'