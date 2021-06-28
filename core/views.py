from django.shortcuts import render, redirect
from core.forms import FormAluno, FormTurma, FormMateria, FormResultado
from core.models import Aluno, Turma, Materia, Resultado
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'core/index.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required
def cadastro_aluno(request):
    if request.user.is_staff:
        form = FormAluno(None or request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno cadastrado com sucesso!")
            return redirect('url_listagem_alunos')
        contexto = {'form' : form,
                    'texto_title': 'CadAlu',
                    'texto_titulo':'Cadastro Aluno',
                    'texto_botao':'Cadastrar',
                    'url_voltar':'url_principal'
                    }
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


@login_required
def listagem_alunos(request):
    try:
        if request.user.is_staff:
            if request.POST and request.POST['aluno_input']:
                dados = Aluno.objects.filter(nome=request.POST['aluno_input'])
            else:
                dados = Aluno.objects.all()
            contexto = {'dados': dados}
            return render(request, 'core/listagem_alunos.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def exclui_aluno(request, id):
    try:
        if request.user.is_staff:
            obj = Aluno.objects.get(id=id)
            if request.POST:
                obj.delete()
                messages.success(request, "Aluno excluido com sucesso!")
                return redirect('url_listagem_alunos')
            else:
                contexto = {'dados': obj.nome, 'id': obj.id, 'url': 'url_listagem_alunos'}
                return render(request, 'core/confirma_exclusao.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def atualiza_aluno(request, id):
    try:
        if request.user.is_staff:
            obj = Aluno.objects.get(id=id)
            form = FormAluno(request.POST or None, request.FILES or None, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Aluno atualizado com sucesso!")
                return redirect('url_listagem_alunos')
            else:
                contexto = {
                    'form': form,
                    'texto_title': 'AtuAlu',
                    'texto_titulo':'Atualização Aluno',
                    'texto_botao':'Atualizar',
                    'url_voltar':'url_listagem_alunos'
                }
                return render(request, 'core/cadastro.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def cadastro_turma(request):
    if request.user.is_staff:
        form = FormTurma(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Turma cadastrada com sucesso!")
            return redirect('url_listagem_turmas')
        contexto = {'form' : form,
                    'texto_title': 'CadTurm',
                    'texto_titulo':'Cadastro Turmas',
                    'texto_botao':'Cadastrar',
                    'url_voltar':'url_principal'
                    }
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


@login_required
def listagem_turmas(request):
    try:
        if request.user.is_staff:
            if request.POST and request.POST['turma_input']:
                dados = Turma.objects.filter(serie=request.POST['turma_input'])
            else:
                dados = Turma.objects.all()
            contexto = {'dados': dados}
            return render(request, 'core/listagem_turmas.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def exclui_turma(request, id):
    try:
        if request.user.is_staff:
            obj = Turma.objects.get(id=id)
            if request.POST:
                obj.delete()
                messages.success(request, "Turma excluida com sucesso!")
                return redirect('url_listagem_turmas')
            else:
                contexto = {'dados': obj.serie, 'id': obj.id, 'url': 'url_listagem_turmas'}
                return render(request, 'core/confirma_exclusao.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def atualiza_turma(request, id):
    try:
        if request.user.is_staff:
            obj = Turma.objects.get(id=id)
            form = FormTurma(request.POST or None, request.FILES or None, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Turma atualizada com sucesso!")
                return redirect('url_listagem_turmas')
            else:
                contexto = {
                    'form': form,
                    'texto_title': 'AtuTurm',
                    'texto_titulo':'Atualização Turma',
                    'texto_botao':'Atualizar',
                    'url_voltar':'url_listagem_turmas'
                }
                return render(request, 'core/cadastro.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def cadastro_materia(request):
    if request.user.is_staff:
        form = FormMateria(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Matéria cadastrada com sucesso!")
            return redirect('url_listagem_materias')
        contexto = {'form' : form,
                    'texto_title': 'CadMateria',
                    'texto_titulo':'Cadastro Materias',
                    'texto_botao':'Cadastrar',
                    'url_voltar':'url_principal'
                    }
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


@login_required
def listagem_materias(request):
    try:
        if request.user.is_staff:
            if request.POST and request.POST['materia_input']:
                dados = Materia.objects.filter(nome=request.POST['materia_input'])
            else:
                dados = Materia.objects.all()
            contexto = {'dados': dados}
            return render(request, 'core/listagem_materias.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def exclui_materia(request, id):
    try:
        if request.user.is_staff:
            obj = Materia.objects.get(id=id)
            if request.POST:
                obj.delete()
                messages.success(request, "Matéria excluida com sucesso!")
                return redirect('url_listagem_materias')
            else:
                contexto = {'dados': obj.nome, 'id': obj.id, 'url': 'url_listagem_materias'}
                return render(request, 'core/confirma_exclusao.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def atualiza_materia(request, id):
    try:
        if request.user.is_staff:
            obj = Materia.objects.get(id=id)
            form = FormMateria(request.POST or None, request.FILES or None, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Matéria atualizada com sucesso!")
                return redirect('url_listagem_materias')
            else:
                contexto = {
                    'form': form,
                    'texto_title': 'AtuMateria',
                    'texto_titulo':'Atualização Matéria',
                    'texto_botao':'Atualizar',
                    'url_voltar':'url_listagem_materias'
                }
                return render(request, 'core/cadastro.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def cadastro_resultado(request):
    if request.user.is_staff:
        form = FormResultado(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Resultado cadastrado com sucesso!")
            return redirect('url_listagem_resultados')
        contexto = {'form' : form,
                    'texto_title': 'CadRes',
                    'texto_titulo':'Cadastro Resultados',
                    'texto_botao':'Cadastrar',
                    'url_voltar':'url_principal'
                    }
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/NaoAutorizado.html')


@login_required
def listagem_resultados(request):
    try:
        if request.user.is_staff:
            if request.POST and request.POST['resultado_input']:
                dados = Resultado.objects.filter(idAluno__nome=request.POST['resultado_input'])
            else:
                dados = Resultado.objects.all()
            contexto = {'dados': dados}
            return render(request, 'core/listagem_resultados.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def exclui_resultado(request, id):
    try:
        if request.user.is_staff:
            obj = Resultado.objects.get(id=id)
            if request.POST:
                obj.delete()
                messages.success(request, "Resultado excluido com sucesso!")
                return redirect('url_listagem_resultados')
            else:
                contexto = {'dados': obj.idAluno, 'id': obj.id, 'url': 'url_listagem_materias'}
                return render(request, 'core/confirma_exclusao.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})


@login_required
def atualiza_resultado(request, id):
    try:
        if request.user.is_staff:
            obj = Resultado.objects.get(id=id)
            form = FormResultado(request.POST or None, request.FILES or None, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Resultado atualizado com sucesso!")
                return redirect('url_listagem_resultados')
            else:
                contexto = {
                    'form': form,
                    'texto_title': 'AtuRes',
                    'texto_titulo':'Atualização Resultados',
                    'texto_botao':'Atualizar',
                    'url_voltar':'url_listagem_resultados'
                }
                return render(request, 'core/cadastro.html', contexto)
        else:
            return render(request, 'core/NaoAutorizado.html')
    except Exception as erro:
        return render(request, 'error.html', {'msg': 'Erro ao executar esta operação!', 'obj': erro})

