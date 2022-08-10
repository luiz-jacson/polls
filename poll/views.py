import math
from msilib.schema import Class
from tkinter.messagebox import QUESTION
from django.shortcuts import redirect, render
from django.http import request
from django.urls import reverse_lazy,reverse
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

    
        

def n_paginas(lista_perguntas):
    num = lista_perguntas.count()
    return math.ceil(num/10)


def Home(request):
    if request.method == 'GET':
        lista_perguntas = Pergunta.objects.all()
        npaginas = n_paginas(lista_perguntas)
        lista_perguntas = Pergunta.objects.all()[:10]
        context = {
            'perguntas':lista_perguntas,
            'paginas':[x+1 for x in range(0,npaginas)]
        }
        return render(request, 'home.html', context)
    elif request.method == 'POST' and  request.POST.get('procurar'):
        lista_perguntas = Pergunta.objects.all().filter(texto_pergunta__icontains = request.POST.get('pergunta_procurada'))
        context = {
            'perguntas':lista_perguntas
        }
        return render(request, 'home.html', context)


def Home_pagina(request,pagina):
    if request.method == 'GET':
        lista_perguntas = Pergunta.objects.all()
        npaginas = n_paginas(lista_perguntas)
        lista_perguntas = Pergunta.objects.all()[((pagina-1)*10):(pagina*10)]
        context = {
            'perguntas':lista_perguntas,
            'paginas':[x+1 for x in range(0,npaginas)]
        }
        return render(request, 'home_pagina.html', context)
    elif request.method == 'POST' and  request.POST.get('procurar'):
        lista_perguntas = Pergunta.objects.all().filter(texto_pergunta__icontains = request.POST.get('pergunta_procurada'))
        context = {
            'perguntas':lista_perguntas
        }
        return render(request, 'home_pagina.html', context)


        


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
    
    
    
    



