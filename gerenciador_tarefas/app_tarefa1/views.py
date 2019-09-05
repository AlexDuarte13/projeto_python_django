from django.shortcuts import render


# Create your views here.

def listar_tarefas(request):
    nome_tarefa = "Aula Treina Web"
    return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})
