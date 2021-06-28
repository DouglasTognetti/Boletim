from django.forms import ModelForm
from core.models import Aluno, Turma, Materia, Resultado


class FormAluno(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'


class FormTurma(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'


class FormMateria(ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'


class FormResultado(ModelForm):
    class Meta:
        model = Resultado
        fields = '__all__'



