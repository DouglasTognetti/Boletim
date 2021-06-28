"""Boletim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import home, Registrar, cadastro_aluno, listagem_alunos, exclui_aluno, \
     atualiza_aluno, cadastro_turma, listagem_turmas, exclui_turma, atualiza_turma, \
     cadastro_materia, listagem_materias, exclui_materia, atualiza_materia, \
     cadastro_resultado, listagem_resultados, exclui_resultado, atualiza_resultado


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='url_principal'),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('cadastro_aluno/', cadastro_aluno, name='url_cadastro_aluno'),
    path('listagem_alunos/', listagem_alunos, name='url_listagem_alunos'),
    path('exclui_aluno/<int:id>', exclui_aluno, name='url_exclui_aluno'),
    path('atualiza_aluno/<int:id>/', atualiza_aluno, name='url_atualiza_aluno'),
    path('cadastro_turma/', cadastro_turma, name='url_cadastro_turma'),
    path('listagem_turmas/', listagem_turmas, name='url_listagem_turmas'),
    path('exclui_turma/<int:id>', exclui_turma, name='url_exclui_turma'),
    path('atualiza_turma/<int:id>/', atualiza_turma, name='url_atualiza_turma'),
    path('cadastro_materia/', cadastro_materia, name='url_cadastro_materia'),
    path('listagem_materias/', listagem_materias, name='url_listagem_materias'),
    path('exclui_materia/<int:id>', exclui_materia, name='url_exclui_materia'),
    path('atualiza_materia/<int:id>/', atualiza_materia, name='url_atualiza_materia'),
    path('cadastro_resultado/', cadastro_resultado, name='url_cadastro_resultado'),
    path('listagem_resultados/', listagem_resultados, name='url_listagem_resultados'),
    path('exclui_resultado/<int:id>', exclui_resultado, name='url_exclui_resultado'),
    path('atualiza_resultado/<int:id>/', atualiza_resultado, name='url_atualiza_resultado'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
