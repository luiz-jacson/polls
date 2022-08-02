from msilib.schema import Class
from tkinter.messagebox import QUESTION
from django.shortcuts import render
from django.http import request
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Pergunta, Resposta


def Create_poll(request):
    if request.method == 'GET':
        return render(request, 'create_poll.html')
    elif request.method == 'POST' and request.POST.get('create_poll'):
        quantidade = request.POST.get('qtde')
        pergunta = request.POST.get('texto_pergunta')
        pergunta_criada = Pergunta.objects.create(texto_pergunta = pergunta)
        print(int(quantidade))
        for c in range(0,int(quantidade)):
            alternativa = request.POST.get(f'texto_alternativa{c+1}')
            Resposta.objects.create(fk_id_pergunta = pergunta_criada, texto_resposta = alternativa)
        return render(request, 'create_poll.html')
    elif request.method == 'POST' and request.POST.get('add_resp'):
        quantidade = request.POST.get('qtde')
        num_alt = [c for c in range(1,int(quantidade)+1)]
        qtde = {'quantidade':num_alt}
        print(qtde['quantidade'])
        return render(request, 'create_poll.html',{'quantidade':qtde['quantidade']})
    
    



