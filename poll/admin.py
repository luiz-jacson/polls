from django.contrib import admin
from .models import Pergunta, Resposta



class RespostaInLine(admin.StackedInline):
    model = Resposta
    extra = 3

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInLine]

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Resposta)