from msilib.schema import Class
from tkinter.messagebox import QUESTION
from django.shortcuts import redirect, render
from django.http import request
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, ListView, DetailView
from .models import Pergunta, Resposta
from django.forms.models import inlineformset_factory
from .forms import RespostaForm, PerguntaForm


def Create_poll(request):
    if request.method == 'GET':
        form_pergunta = PerguntaForm()
        form_resposta_factory = inlineformset_factory(Pergunta, Resposta, form = RespostaForm, extra=3)
        form_resposta = form_resposta_factory()
        context = {
            'form_pergunta' : form_pergunta,
            'form_resposta' : form_resposta,
        }
        return render(request, 'create_poll.html', context)
    elif request.method == 'POST':
        form_pergunta = PerguntaForm(request.POST)
        form_resposta_factory = inlineformset_factory(Pergunta, Resposta, form = RespostaForm)
        form_resposta = form_resposta_factory(request.POST)
        if form_pergunta.is_valid() and form_resposta.is_valid():
            pergunta = form_pergunta.save()
            form_resposta.instance = pergunta
            form_resposta.save()
            return redirect('home')
        else:
            print(form_resposta.is_valid())
            context = {
            'form_pergunta':form_pergunta,
            'form_resposta':form_resposta
            }
            return render(request, 'create_poll.html', context)

    
        




class Home_view(ListView):
    model = Pergunta
    template_name = 'home.html'


def Respostas(request,pk):
    lista_respostas = Resposta.objects.filter(fk_id_pergunta = pk)
    marcado = request.POST.getlist('respostas')
    if request.method == 'POST' and request.POST.get('Votar'):
        for c in marcado:
            resposta = Resposta.objects.get(pk = c)
            resposta.votes += 1
            resposta.save()
        return redirect('result', pk)
    return render(request, 'vote.html',{'respostas':lista_respostas})

def Resultados(request, pk):
    lista_respostas = Resposta.objects.filter(fk_id_pergunta = pk)
    pergunta = Pergunta.objects.filter(pk = pk)
    return render(request, 'result.html',{'respostas':lista_respostas, 'pergunta':pergunta})
    
    
    
    



